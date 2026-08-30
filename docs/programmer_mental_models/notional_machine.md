# Notional Machine
程序员为了理解程序执行而在脑中使用的抽象机器。
# notional machine vs computation model
Computation model 定义计算世界的语义规则；notional machine 把这些规则组织成一台程序员可以在脑中模拟的假想机器。

- computation model 回答：计算遵循什么规则？

- notional machine 回答：程序执行时，我应该想象有什么东西在怎样运转？

Notional machine 比 computation model 更直接符合需求：重建高级程序员在阅读、编写和调试程序时，脑中用来推演程序行为的模型。

Computation model 是理论地基，研究**计算**这个概念的primitives；notional machine 是程序员可以实际运行的 mental model。
# Advanced Programmer
I want to reconstruct the layered notional machines that advanced programmers use to predict, debug, and design software systems. Computation models provide the semantic foundations for those notional machines, but my primary goal is practical mental simulation rather than formal language theory.

Different semantic contexts have their own models, and notional machines are executable mental representations used to simulate the dynamic behaviour of those models. A single context may require multiple notional machines, while an end-to-end notional machine may cross several context or abstraction boundaries.

# References
- [Juha Sorva — Notional Machines and Introductory Programming Education](https://dl.acm.org/doi/epdf/10.1145/2483710.2483713)

- Structure and Interpretation of Computer Programs(2022 JavaScript Edition：JavaScript), Harold Abelson、Gerald Jay Sussman

- Concepts, Techniques, and Models of Computer Programming

- Programming Languages: Application and Interpretation, Shriram Krishnamurthi

- Crafting Interpreters, Robert Nystrom

- Computer Systems: A Programmer’s Perspective, Randal Bryant、David O’Hallaron

- Operating Systems: Three Easy Pieces, Remzi Arpaci-Dusseau、Andrea Arpaci-Dusseau

- Designing Data-Intensive Applications, Martin Kleppmann, Chris Riccomini(second version) - database

- You Don’t Know JS Yet, Kyle Simpson

