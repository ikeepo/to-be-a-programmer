---
  tags：
    - mental model
---
# Animations
# Concepts
- A CSS animation consists of two main components: the @keyframes rule and the animation property.

    - The @keyframes rule defines the stages and styles of the animation. 

    - Animation property: `animation`(a shorthand for several individual properties)
        
        - `animation-name`

        - `animation-duration`
    values:

        - `animation-timing-function` timing function (dictates when the movement speeds up or slows down): `linear, ease-in, ease-out, ease-in-out`

        - `animation-delay`

        - `animation-iteration-count`

        - `animation-direction`

        - `animation-fill-mode`

        - `animation-play-state`

# Mental Model
css animation效果，类似这种功能，首先需要渲染引擎具备这种功能，才能通过调用animation的关键字和参数来实现。

实际上一种语言或者工具，类似css，其功能取决于他的解释器（渲染引擎）具备的内置功能。

**所有的声明式代码（CSS、HTML、SQL、JSON 配置），本质上都只是传给底层渲染引擎或执行引擎的“参数字典”。**


# Declarative Offloading
css animation本质上是将一些js功能内置、编译到css渲染引擎中，只暴露出这些功能的接口，是的用户可以通过简单配置实现原本需要手动编写js代码的功能。

这种演化行为叫做Declarative Offloading.

Once the browser parses the CSS rules, it identifies declarative animations involving GPU-accelerated properties (like transform and opacity). Instead of running these on the **Main Thread**—where JavaScript execution and layout calculations happen—the rendering engine offloads the animation pipeline directly to the **Compositor Thread**.

This allows the GPU to compute intermediate frame interpolation independently, ensuring silky-smooth 60fps/120fps animations even if the Main Thread is heavily blocked by JavaScript.

```shell
┌─────────────────────────────────────────────────────────────┐
│                 BROWSER TAB (Renderer Process)              │
│                                                             │
│   ┌─────────────────────────────────────────────────────┐   │
│   │ Main Thread                                         │   │
│   │ ├── JavaScript Engine (V8)                          │   │
│   │ ├── DOM & CSSOM Parsing                             │   │
│   │ └── Layout & Paint Calculations                     │   │
│   └──────────────────────────┬──────────────────────────┘   │
│                              │ passes pre-rendered layers   │
│                              ▼                              │
│   ┌─────────────────────────────────────────────────────┐   │
│   │ Compositor Thread                                   │   │
│   │ └── Moves/scales layers & sends draw calls to GPU   │   │
│   └──────────────────────────┬──────────────────────────┘   │
└──────────────────────────────┼──────────────────────────────┘
                               ▼
                        [ System GPU ]
```


- As a general rule, avoid any content that flashes more than three times per second.


