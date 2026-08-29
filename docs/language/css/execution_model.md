# Execution Model
This is the CSS domain model knowledge crunching.
# CSS's Two levels
There are two levels of CSS:

- CSS Descriptive Language

CSS vocabulary, they build map "CSS expression → observable result".
This section is provided by the general courses.

- CSS Execution Model

State change, Association change, Invalidation propagation.
This section is the primary focus of this article.
# Entrance
[Tali Garsiel](https://webplatform.github.io/docs/concepts/Internet_and_Web/how_browsers_work/)’s 'How Browsers Work' primary focuses on browser execution, even though it was published in 2011. CSS, specifically, is processed within the rendering engine.

We are using this section as a starting point to break down the CSS execution model.

### Find Objects
Find objects, every object has specific lifecycle, associations, transformation, invariant.

To simplify things, I will present the knowledge visually rather than using text to describe the model I am building.

### Start from a minimal workflow
[ Flowcharts ](https://en.wikipedia.org/wiki/Flowchart) will be used as the primary format for visual output. Choose [React Flow](https://reactflow.dev) as the tool, need to learn this first.

React + TS + React Flow.




