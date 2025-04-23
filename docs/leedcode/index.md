# LeedCode Thought
Word in this chapter has much more chance to be wrong.
They are not check by the tool, just my intuitive english expression.

# Rules
## R1: Five Practice One Knowledge Search
## R2: Five Knowledge Search One Think
## R3: When you see Data Structure, you see memory
Which means data structure carries informations.
# Why LeedCode
Only body is yours, the knowledge belong the practicer who write them.
Which mean you should code first, then to read other people's thought, it's a kind of discussion.
If you want to read book before code(practice to the body), you can only need to read the headers and first and last sentence, to know the basic concepts in that domain.
This is really the important point to be efficient and right, if there is right or wrong.
思想并不能用于指导行为，除非它是基于自身行为进行分析总结之后的抽象，也就是说，思想主要起作用于对现实行为的分析、解释，继而或许有能提供指导的作用，但切不可颠倒顺序，那种场景叫做：内耗。
# Mathmatical Mindset Helpful to Programming
## Sort
Sort带来信息；
加速查找；
- 取中间值
$mid = low + (high - low) / 2$ rather $high / 2$
## Compare
比较带来顺序、带来信息；
## 循环
循环的是同一个层面的数据，这里有一个同层级的概念；
## 递归
更新后遇到同样的位置；
还有一种形式，是将同层级的数据放到一个queue中实现递归+循环；
## 层级
同一个层级可以放到一个循环结构中，跟递归结合后，就可以循环扩展，通过queue实现，这个实在是太漂亮了。
## `if-else`
思考的完备性，if else需要完整考虑所有可能性；
或者说ifelse是为了完备所有可能性而存在的，所有分支都应该完备所有可能性；
## cycle
- modulo
cycle give context to the cycle.
## Memoization
Used for optimization;
Comes from some subproblem is calculated multitimes.

# Procedure (DDD)
### Extract Information
- Literal
- DataStructure
### Classification
### Algorithm

### Concept Definition
Make clear about every concept's defination, clear means you can tell that to other people, make them understand rather you.
### Element
- variable
包括初始、最终输出结果
- constraint
业务场景限制；
### 业务逻辑
Element之间的关联关系
### Domain
Element and relationship would define a domain.
### 从结果向前推
确定结果出现在哪几种场景，对场景进行完备性构建，也就是if else里面的完备性；
