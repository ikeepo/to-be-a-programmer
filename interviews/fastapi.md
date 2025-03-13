# How FastAPI is different from Flask and Django
1. Asynchronous, out of box. FaskAPI leverages Python's asyncio and tools like Starlette and Pydantic.
Flask is synchronos by default. Django is more monolithic and traditionally synchronous.
2. FaskAPI offers automatic generation of interactive  API docs using OpenAPI and ReDoc, based on its integration with Pydantic for data validation. This is a huge advantage when working with teams. Flask and Django need additional work .
3. type-hinting and dependency injection system make it more developer-friendly and less error-prone.
data validation reduce boilerplate code. Flask leaves this to the developer, and Django provides a full ORM and a batteries-included approach, hich ia great for large-scale apps but can feel heavy for API-only projects.
Flask is simple, and Django is comprehensive but heavier framework.
# Difference between WSGI and ASGI
They are both server-gateway interface in Python, but they serve different purposes.
WSGI Web Server Gateway Interface, is a synchronous standard for Python web app, introduced in PEP 3333. it's designed to connect frameworks like Flask and Django;
WSGI works by handling one request at a time per worker process, which makes it simple and reliable but limits its ability to handle high concurrency or long-lived connection like WebSockets.
ASGI Asynchronous Server Gateway Interface, is the successor to WSGI, designed for Asynchronous programming. It supports Python's asyncio and allows frameworks like FastAPI and Starlett to process multiple requests concurrently within a single process.
- server-gateway interface are specifications that define how web servers communicate with web applications or frameworks.
gateway is like a gate between the web server and the application, controlling how requests flow in and out.
# server vs framework
A server is the software that listens for incoming requests - like HTTTP requests from traders - and sends back responses. Gunicorn, Uvicorn, Nginx.  When you run a server, it's the thing that stays active, waiting for clients to connect.
A framework, is a set of tools and libraries that helps you write the appication logic - what happens when a request arrives. It's not a server itself, it's the code that defines routes, processes data, and generates responses.
# Uvicorn  vs Nginx
Uvicorn is a ASGI server, Nginx is a web server;
An ASGI server is a specialized server designed to run Asynchronous Python app that follow the ASGI specification.
A web server, like Nginx or Apache, is a more general-purpose tool that handles HTTP trafiic at a lower level. It excels at tasks like serving static content, managing thousands of concurrent connections, load balancing, or acting as a reverse proxy to forward requests to an ASGI server.
In a typical production setup, network requests first hit Nginx, which acts as a web server and reverse proxy, then Nginx decides what to do with them - either serving static content directly or forwarding dynamic requests to an ASGI server.
- Reverse Proxy
It is a server that sits between clients and backend servers, forwarding client requests to the appropriate backend and returing the responses to the clients.
REVERSE is a direction, 在服务器一侧，帮客户从服务器内部做处理，对于服务器来说是向内，所以叫反向代理；
正向代理是在客户端那一侧，对于客户端来说，是向外处理；
# WSGI worker thread
In WSGI , a 'worker' is a process or thread that handles incoming requests, and its threading model depends on the server configuration.
Gunicorn use multiple workers or threads to achieve concurrency.
In Gunicorn , a worker is a separate process spawned to run the WSGI application, each worker can handle one request at a time synchronosly. You can configure multiple workers, where each runs in its own process, leveraging multi-core CPUs.
In Gunicorn, you can spawn multiple threads in each worker process, but still synchronos - each thread processes one request fully before moving to the next.
In Gunicorn, starting multiple workers means spawning multiple processes, but they all run the same Flask app instance, just in a separate processes. Each worker loads the same application code, including all endpoints, and handles incoming requests independently.
# ASGI
Uvicorn leverages Python's asyncio library to process multiple requests Asynchronous within a single process by default.
Uvicorn starts a single event loop - a core feature of asyncio - that listens for incoming requests on a port, like 8000. Each request is treated as an async task.
Uvicorn can also scale with multiple processes using the --workers option, where each process runs its own event loop, similar to Gunicorn's multi-process model.
# FastAPI's inbuilt client
FastAPI provides a built-in test client through the TestClient class from the starlett.testclient module.
It allows you to simulate HTTP requests - like GET or POST - to your FastAPI app in memory, making it fast and convenient for unit or integration tests.
It's synchronous by default, but it works seamlessly with FastAPI's async endpoints.
# FastAPI doesn't support Python 2
# middleware
In FastAPI, it's a layer of code that sits between the incoming request and the application's reoute handlers, allowing you to process requests or responses globally.
It's built on Starlette's middleware system and can be used for tasks like logging, authentication, or modifying headers.
It's a flexible mechanism where you define your own logic to process requests and responses globally.
###  CORSMiddleware
built-in middleware in FastAPI, inherited from Starlette, designed to handle Cross-Origin Resource Sharing. It allows you to control which external domains - or origins - can access your API, which is crucial when a frontend needs to call your endpoints.
Accept header, regex,

Some are added to endpoints, some are added to app level.
Middlewares have a certain order which is a synchronos manner, but the underlying function can be defined both synchronos or asynchronos.
#### Cross-Origin
An origin is defined by the combination of protocol, domain and port.
If these differ between the requester and the target, it's a cross-origin request.
Cross-Origin refers to a situation in web development where a resource, like a webpage or script, tries to access another reource.
Browsers enforce a Same-Origin Policy for security, blocking such requests unless the server explicitly allows them via CORS headers, like `Access-Control-Allow-Origin`.
### FastAPI dependencies
It allows you to inject resuable logic or resources into your route handlers, promoting code resue and modularity.
It's built into the framework's dependency injection system, where you define a function - sync or async - that FastAPI calls automatically before executing an endpoint.

dependency injection system is the underlying mechanism FastAPI provides to manage and execute dependencies which are specific functions or logic.
### dependency  vs  middleware
They seem similar because they both handle pre-processing logic, but they seve different purposes and operate at different levels.
dependency are scoped to specific routes or globally via app.dependency().
middleware default globally,
I use dependency for precision, middleware for broad tasks.
dependency focus on return some data to endpoint, while middleware don't return;
### dependency overwrite, mock dependency
In FastAPI, mocking a dependency and overwriting it are techniques used primarily for testing to isolate and control the behavior of dependices.
mock a dependency comes from the pytest fixtures, and dependency overwriting is a FastAPI specific feature using `app.dependency_overrides`, it allows you temporarily replace a dependency with a mock version during testing.
### Pydantic
runtime type checking;
It has three mean functionality:
- data validation
It ensuring that incoming data is automatically validated and parsed into structured objects.
- serialization
handle deserialization from requests and serialization for responses;
- type safety
- generate OpenAPI schemas
It powers the FastAPI's automatic documentation.
### 协程coroutines
Coroutines in FastAPI are asynchronous functions defined with async def, enabling non-blokcing execution using Python's asyncio lib, They're fundamental to FastAPI's ASGI architechture, allowing it to handle multiple requests concurrently within a single thread, which is ideal for I/O-bound tasks like a trader API wairing on database queries or external services.
A coroutine pauses at await statements, yielding control back to the event loop to process other tasks until the awaited operation completes.
- coroutine vs function
A coroutine is a special type of function defined with async def, while a regular function is defined by def.
A coroutine supports Asynchronous execution with await, allowing it to pause and yield control back to the event loop for non-blocking behavior, whereas a regular function runs synchronously, blocking until it completes.
coroutine is working within a single thread, without OS-level context switching.
Coroutines share the thread's execution time.  and it's user level schedule.
function don't release control, until completion.
### background tasks
In FastAPI, background tasks allow you to run time-consuming operations after sending a response to the client, leveraging the BackgroundTasks class.
It's great for tasks like sending emails, logging trades, or processing data that shouldn't delay the client's response.
It's used for handling unnecessary logic Asynchronously;



# Refs
1. [What is FastAPI | FastAPI Mock Interview | Interview Questions for Senior FastAPI Developers](https://www.youtube.com/watch?v=qLdqNEjYQtI)
