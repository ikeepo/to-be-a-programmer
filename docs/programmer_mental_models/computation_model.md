
# Computation model
不局限于编程语言的更高层级的对于计算语义的抽象,一套关于计算世界的物理定律。
编程语言根据自己的目标，选择并组合不同的 computation concepts，形成其支持的 computation models。
编程语言的设计者、实现者和程序语言理论研究者，是最显式地使用 computation model 的人群。
Computation model 是对“计算可以由哪些基本对象组成，以及计算如何推进”的精确抽象。
Computation concepts 是一组有生成力的primitives，可以推演出程序行为；

数学提供规律，computation model 提供世界，算法提供策略，编程语言提供表达界面。

A computation model is not a semantic-level algorithm. It is a semantic framework that defines the basic entities, operations, and execution rules within which algorithms can be expressed. Language designers explicitly select and combine computational concepts according to their design goals, but advanced programmers also benefit from these models because they reveal the alternatives hidden behind particular language and framework APIs.
# Computation Model对于application programmers的作用
1. 这个世界中的基本实体是什么？

2. 哪些东西包含 state

3. state 由谁拥有？

4. 哪些操作会导致 state transition？

5. execution order 有什么保证？

6. computation 如何通信和同步？

7. failure 如何传播和恢复？

8. 哪些是本质机制，哪些只是 surface syntax？

# Refs
- Concepts, Techniques, and Models of Computer Programming

- Structure and Interpretation of Computer Programs, Harold Abelson、Gerald Jay Sussman、Julie Sussman

- The Programmer’s Brain, Felienne Hermans

