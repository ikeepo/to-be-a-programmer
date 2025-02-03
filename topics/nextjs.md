# tailwind

## @tailwind base;

引入tailwind基础样式，components是内置组件库，utilities是工具类；

## @tailwind base是tailwind csss语法还是Postcss语法，这两者是什么关系，是通过哪个插件来解析

## 是否必须引入

## global.css内容是如何解析的，解析成plate css是什么样子的

## Next.js will automatically install the necessary packages and configure Tailwind in your application. 指的是做了哪些操作

## 与inline styles相比tailwind增加了响应式功能及对用户动作的反馈

可以理解为把js的一部分功能写到了tailwind中？

## [antialiased](https://tailwindcss.com/docs/font-smoothing) 是什么意思

## . It's not necessary to use this class, but it adds a nice touch.

What the nice touch mean?

## Now it's your turn! In your fonts.ts file, import a secondary font called Lusitana and pass it to the <p> element in your /app/page.tsx file. In addition to specifying a subset like you did before, you'll also need to specify the font weight.

WHY?

## If you're unsure what weight options to pass to a font, check the TypeScript errors in your code editor.

WHY?

## clsx 存在的必要

tailwind内置的utility可以对用户的动作&屏幕尺寸进行相应；
clsx是对变量值进行相应；

# nextjs 结构设计

## nextjs detects if your project use TS and automatically install s the necessary packages and configuration

# pnpm vs npm

npm保存副本，而pnpm在全局维护一份代码，各个项目上使用硬链接或符号链接；  
符号链接就是软连接；  
直接的依赖关系使用硬链接，node_modules里依赖关系使用软连接；  
npm 是下载完整的依赖关系在每个独立的项目中；

## pnpm run dev VS. pnpm dev

pnpm run 会在package.json中查找scripts字段下的脚本命令；  
pnpm dev是一种更简介的操作方式，我猜想跟那个日本程序员的习惯类似；

# ``<body className={`${inter.className} antialiased`}>{children}</body> 详解语法``

- 模板字符串`${}`
  动态拼接字符串， 反引号包裹字符串，`${}` 插入变量或表达式；
  这是JS ES6的语法；

# md:block

utility class, block用于将元素的display设置为block，独占一行；  
md: 是一个响应式前缀，表示在中等屏幕尺寸768px以上是应用相应的样式；

# page.tsx is a special Next.js file that exports a React component.

It's required for the **route** to be accessible;  
创建一个page就可以理解为创建一个路由；

# layout.tsx的好处

# [split code by route](https://nextjs.org/learn/dashboard-app/navigating-between-pages#automatic-code-splitting-and-prefetching)

which means that pages become isolated. If a certain page throws an error, the rest of the applciation still work.  
依据route划分也就是依据跳转划分，这样每次跳转只需要改变被route划分好的那部分代码；  
And whenever <Link> components appear in the browser's viewport, Next.js automatically prefetches the code for the linked page in the background.

1. Browser's Viewport 是什么

# prefetching

whenever <Link> appear in the browser's viewport, Next.js automatically prefetches the code for the linked page in the background.

# [request waterfalls](https://nextjs.org/learn/dashboard-app/fetching-data#what-are-request-waterfalls)

a waterfall refers to a sequence of network requests that depend on the completion of previous requests.
you need a waterfall when you want a condition to be satisfied before making the next request.

# [Promise.all()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)

JS的语法；

1. takes an iterable of promosies as input ;
2. returns a single Promise;
3. returns promise fulfilss when all of the input's promises fulfill;
4. rejects when any of the input's promises rejects ;

# Faster Websites - Prerendered content can be cached and globally distributed. This ensures that users around the world can access your website's content more quickly and reliably.

这个cached指的是缓存在哪里？  
内容分发网络（CDN）的缓存节点上，网站拥有者为这些CDN付费，首次缓存可以是网站拥有者配置的主动缓存，也可以是用户使用后的被动缓存；缓存的核心是将一些静态资源提前放置在离用户较近的服务器上；

# static rendering vs dynamic rendering

# streaming

break down a route into smaller "chunks" and progressively stream them from server to the client as they become ready;
each component can be considered as a chunk;

> 每个组件都可以被认为是一个chunk；？反过来一样？
> 是的，每个租金啊斗殴可以被认为是一个chunk；每个chunk也可以被认为是一个组件；  
> chunk的划分一般是按照逻辑，而非容量；

| page level  | component  |
| ----------- | ---------- |
| loading.tsx | <Suspense> |

# Suspense是一个React特性，用于处理异步数据加载；

主要起作用的属性是fallback，用作在异步数据加载时显示的内容；

# route groups

用()包裹，()内的路由不显示在URL path中；

# [Route Handlers](https://nextjs.org/docs/app/building-your-application/routing/route-handlers#dynamic-functions)

app内使用，可以嵌套文件夹使用；  
但是route.js文件不可以跟page.js文件混用；

## dynamic function

if you call a dynamic function in a route , the entire route becomes dynamic;  
运行时获取数据或引入动态行为的函数；

# PPR- Partial Prerendering

you don't need to change your code to use it.

# 路由是client side or server side?

两者皆可，客服端路由通过js实现，无需全部重载整个页面的HTML，只是部分位置渲染；  
服务端路由通过后端实现，页面内容全部重构；

## client-side navigation

routing 是个更广泛的概念，navigation是指具体的跳转动作；

- [usePathname](https://nextjs.org/docs/app/api-reference/functions/use-pathname)
  Reading the current URL from a Server Component is not supported.

## hooks只能用于client side么？

不一定，也可以用于服务器端渲染（SSR）；  
Hooks是在组件渲染时运行，useEffect只能用于client side；

## [debouncing](https://nextjs.org/learn/dashboard-app/adding-search-and-pagination#best-practice-debouncing)

Debouncing is a programming practice that limits the rate at which a function can fire.

1. When an event that should be debounced occurs, a timer starts;
2. If a new event occurs before the timer expires, the timer is reset;
3. If the timer reaches the end of its countdown, the debounced function is executed.

# Server Actions

> 就是get请求后面那个函数么？--不是
> Server Actions 是指在Server Components中运行的函数，在服务器端运行，但是可以在客户端调用；  
> 这里的要点是指在客服端调用，但是并不重新加载页面；  
> get那个叫传统的HTTP请求；  
> Server Action无需服务端返回响应；

## Server COmpoents指的是什么？

1. async function create() {'use server'} 这算什么？是个函数不是组件？
   这是一个Server Actions；  
   并不强制是异步的，单一般是异步的；
2. An advantage of invoking a Server Action within a Server Component is progressive enhancement - forms work even if JavaScript is disabled on the client.
   JS disabled是什么意思？ 浏览器的JS被禁用，一些用户操作无法执行；  
   但是Server Action是在服务器端执行的，所以不受JS影响；

3. Nextjs的教程本质是介绍Nextjs内置的组件？以及为什么设置这些组件的逻辑？

4. Server Actions are also deeply integrated with Next.js caching. When a form is submitted through a Server Action, not only can you use the action to mutate data, but you can also revalidate the associated cache using APIs like revalidatePath and revalidateTag.  
    Server Action是发生在Server, 而Cache是缓存在client 本地，那怎么校验缓存？需要经过几次前后端的通信？是通过虚拟树来对比还是什么其他的方式？
   这里的缓存一般是指服务器端的缓存，不是客户端的缓存；  
   revalidatePath一般是指确保缓存数据更新，而不是比较；
5. To start, inside the /invoices folder, add a new route segment called /create with a page.tsx file:  
    为什么叫route segment? 是指路由的一部分么？  
   Nextjs中使用文件系统路由，segment就是一个路径段；

A dynamic [Route Segment](https://nextjs.org/docs/app/building-your-application/routing/dynamic-routes) can be created by wrapping a folder name in square brackets.

6. 如何判定是一个Server Component还是一个Server Action？
   a. by adding the 'use server' you mark all the exported functions within the file as Server Actions.  
    b. you can also write Server Actions directly inside Server Components by addin g'use server' inside the action
   use server是用来标记函数的，不是组件；  
   server component是指在服务器端运行、渲染成HTML，然后返回给客户端；  
   前端组件一般是通过JS运行，响应客户反馈，通过use client标记；  
   use client针对组件，use server针对函数；  
   分为前后端组件，主要是为了打包时候区分；

7. Pages are [Sever Components](https://nextjs.org/docs/app/api-reference/file-conventions/page) by default;

## [Server Functions](https://react.dev/reference/rsc/use-server)

Add 'use server' at the top of and async functionbody to mark the function as callable by the client. which is called Server Function.

## use server是React的功能，不是nextjs的？

是nextjs的；

## FormData 是web api, 是一个interface, 是一个object；

web api提供的一个接口，用于将一个html中表单数据转换成键值对对象数据；

## [Accessibility](https://nextjs.org/learn/dashboard-app/improving-accessibility#what-is-accessibility)

键盘绑定、语义化标签等让不同的用户都能正常访问网页，比如vim用户；

## [authentication and authorization](https://nextjs.org/learn/dashboard-app/adding-authentication#authentication-vs-authorization)

Authentication is about making sure the user is who they say they are, and authorization decides what parts of the app they are allowed to access.

## [Middleware](https://nextjs.org/docs/app/building-your-application/routing/middleware)

> Middleware是专门指鉴权的专有名词么？
> 跟用一个函数包裹另一个函数有什么区别？

Middleware是Nextjs的概念，还是React的概念，亦或JS的？

## nextjs编程有大量的工作是脚手架拼图，并不是自己写的逻辑，而是已有功https://nextjs.org/learn/dashboard-app/adding-metadata能的配置？

## [metadata](https://nextjs.org/learn/dashboard-app/adding-metadata)

### Additionally, metadata like Open Graph improves the appearance of shared links on social media, making the content more appealing and informative for users.

Open Graph是什么？是一个协议么？

### metadata 类型

- title

```html
<title>Page Title</title>
```

- desctiption metadata

```html
<meta name="desccription" content="This is a description of the page" />
```

- Keyword Metadata

```html
<meta name="keywords" content="keyword1, keyword2, keyword3" />
```

- Open Graph Metadata

```html
<meta property="og:title" content="Title Here" />
<meta property="og:description" content="Description Here" />
<meta property="og:image" content="image_url_here" />
```

- Favicon and Open Graph Image

```html
<meta test />
```

# import { CheckIcon, ClockIcon } from '@heroicons/react/24/outline';

# nextjs是层级嵌套覆盖的结构

layout可以 被下层route继承，直到覆盖修改；
