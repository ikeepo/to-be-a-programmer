# Chapter 1: Function Abstraction
# Concepts
### infix notation
`operand operator operand` contrasts with Scheme's *prefix notation* - `operator operant operant`

### after operator combinations
Function applications are—after operator combinations—the second kind of combination of expressions into larger expressions.
`function-expression(argument-expressions)`
###  left-associative
means that operators of the same precedence are grouped from left to right.

### read–evaluate–print loop (REPL)
an interactive environment that repeatedly performs four steps:

1. Read the expression you enter.
2. Evaluate it.
3. Print the resulting value.
4. Loop back and wait for the next expression.

### Evaluation Process Thinking Models
##### substitution model for function application

-  normal-order evaluation: fully expand and then reduce

- applicative-order evaluation: evaluate the arguments and then apply


