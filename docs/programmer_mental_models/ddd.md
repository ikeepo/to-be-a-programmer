# DDD
[Domain Drive Design](https://en.wikipedia.org/wiki/Domain-driven_design)

以前：

DDD = 给人看的设计方法

现在：

DDD = 给 AI 的“约束提示系统”

DDD 从“设计方法”变成“Prompt Architecture（提示架构）”
# DDD价值演变
核心能力：
1. Bounded Context 设计
划分系统边界
防止语义污染
2. Ubiquitous Language
统一业务语言
防止 AI 误解 domain
3. Aggregate Design
控制一致性边界
控制数据依赖关系

# 程序员角色转变
传统程序员：`需求 → 写代码 → 调试 → 交付`

AI时代程序员: `需求->建模（DDD）->约束 AI生成空间->审查 & 修正结构->系统运行反馈`

不再需要码农，但是需要更多的架构师。横向扩展懂各个领域底层原理的架构师。
而DDD是其中关键的一个认知，用于框定使AI避免幻觉混乱。
