---
  tags:
    - mental model
    - engine
    - engine learning roadmap
    - prompt
    
---
# Declarative Code
css   animation效果，类似这种功能，首先需要渲染引擎具备这种功能，才能通过调用animation的关键字和参数来实现.

实际上一种语言或者工具，类似css，其功能取决于他的解释器（渲染引擎）具备的内置功能.

声明式代码（Declarative Code）让你能“快速用起来”，但只有理解了背后的引擎（Engine Mental Model），你才能“真正用好”。

# Law of Leaky Abstractions

声明式代码（CSS、SQL、React JSX 等）的本意是隐藏复杂性。

`声明式代码 (What) ───► 底层引擎 (How) ───► 懂引擎带来的差异`

!!! info: 程序员的深度学习在学什么？
    这解决了学什么的问题；
    学一门declarative language是要学习底层引擎；
    而引擎本身底层又是硬件优化；
    学习的深度就在于层级的厚度；

$$\text{声明式代码 (What)} \xrightarrow{\text{解释/编译}} \text{引擎 (Engine)} \xrightarrow{\text{拆解/调度}} \text{算法 (Algorithms)} \xrightarrow{\text{指令映射}} \text{硬件电路 (Hardware)}$$

## 引擎 == 算法
算法又有两个纬度：

- 正确性（算对）

- 时空复杂度（算得快）

引擎算法比纯数学算法多了一个纬度：

- 硬件限制

因为“实现”需要基于物理限制，导致面向对象(OOP，纯粹逻辑思考)导向面向数据(DOD, 物理限制/优化)

## 如何学习引擎
并不是逐行读代码，而是了解引擎算法的层级。

学习引擎不是学习代码如何写，而是学习如何隐藏复杂度、如何抽象业务、构造代码结构。

直接阅读引擎doc效率不高，因为它是给代码贡献者写的，默认你是有对应层级的代码编写能力。

`心智模型 ==> 剖析工具 ==> 动手造简易版 ==> 查阅权威资料`

- 构建心智模型

    - How Browsers Work

    - [CS Visualized](https://dev.to/lydiahallie)

    - Designing Data-Intensive Applications

    - Crafting Interpreters

- 剖析工具,利用开发者工具“看到”引擎的运行
  
    - DevTool -- Performance

    - EXPLAIN ANALYZE SQL, Execution Plan

- Toy Project

    - What I cannot create, I do not understand.

- 最后看官方源码/设计文档

    - 架构设计文档

    - Architecture

## 以`transform-origin`为例，穿透到引擎机制
```shell
Role: You are a senior browser engine & system architecture expert. 

Task: Help me deeply understand the concept/property: [INSERT CONCEPT/PROPERTY HERE, e.g., transform-origin / flex-shrink / Event Loop].

Break down the concept into the following 4 structured sections:

1. Mental Model (几何/数学/底层的物理与心智模型):
   - Explain what this concept means beyond the surface API level.
   - Show the underlying math, algorithm, or state transformation happening under the hood.

2. Engine Pipeline (渲染管线与执行路径):
   - Map out where this concept runs (Main Thread, Compositor Thread, GPU, JS Engine, etc.).
   - Explain if/how it affects Layout (Reflow), Paint (Repaint), or Composite steps.

3. DevTools Inspection (如何用开发者工具观察它):
   - Give precise steps on how to use Chrome DevTools (e.g., Performance, Layers, Rendering/Paint Flashing) to "see" this mechanism in action.

4. Toy Project (动手造简易版/纯手写实现):
   - Provide a minimal, zero-dependency code snippet (e.g., using pure JavaScript, Canvas, or low-level logic) that manually mimics/recreates how the engine handles this behavior without relying on the built-in feature itself.
```



# 技术图谱
```shell
┌──────────────────────────────────────────────────────────┐
│ 1. 声明式语言 (Declarative Language)                     │  ← 表达意图 ("我要做什么")
└────────────────────────────┬─────────────────────────────┘
                             │ (解释 / 编译)
┌────────────────────────────▼─────────────────────────────┐
│ 2. 引擎 (Engine)                                         │  ← 逻辑中枢 ("怎么做")
│    - 本质：封装了特定领域的【算法策略】                      │
└────────────────────────────┬─────────────────────────────┘
                             │ (算法优化与映射)
┌────────────────────────────▼─────────────────────────────┐
│ 3. 硬件物理特性 (Hardware Realities)                      │  ← 物理极限 ("算得多快")
│    - 限制：内存带宽、Cache 层级、GPU 算力单元、物理散热     │
└──────────────────────────────────────────────────────────┘
```

# 命令式语言Imperative
```shell
┌────────────────────────────────────────────────────────────────────────┐
│ 声明式语言 (Declarative: CSS, SQL, PyTorch, HTML)                       │
│ ┌────────────────────────────────────────────────────────────────────┐ │
│ │ 程序员：只提需求 (What)                                             │ │
│ ├────────────────────────────────────────────────────────────────────┤ │
│ │ 引擎（内置高阶算法）：完全接管 "如何计算、如何优化、如何调度" (How)      │ │
│ └────────────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼ 转移控制权
┌────────────────────────────────────────────────────────────────────────┐
│ 命令式语言 (Imperative: C, C++, Rust, Go)                               │
│ ┌────────────────────────────────────────────────────────────────────┐ │
│ │ 程序员：必须亲手写算法 (How) ── 手动控制循环、指针、数据结构、内存分配   │ │
│ ├────────────────────────────────────────────────────────────────────┤ │
│ │ 编译器/硬件引擎：辅助优化 (帮你把手写的算法翻译成最优雅的机器指令)      │ │
│ └────────────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────────┘
```

所谓命令式，实际上是程序员部分完成了一定程序的引擎工作，使得程序员可选择空间稍稍往底层进了一步；也就是在写一部分算法工作
