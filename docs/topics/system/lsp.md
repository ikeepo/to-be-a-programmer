# LSP

Barbara Liskov在1987年提出，核心思想是：子类对象必须能够替换其父类对象，而不会影响程序的正确性。
子类应该扩展父类的功能，而不是破坏它的行为。
如果一个函数能正确处理父类对象，那么它也应该能正确处理子类对象，而不需要修改代码。

## python typing

typing默认使用的是nominal typing, 即要求类型显式继承；而非结构化类型检查(from typing import Protocol)。
