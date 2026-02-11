# [mermaid](https://github.com/mermaid-js/mermaid)
Flowchart from text like markdown.
程序流程图
# 如何在Jupyter中使用mermaid
[`mermaid-python` ](https://pypi.org/project/mermaid-python/) 有效；
```python
from mermaid import Mermaid
Mermaid("""
    flowchart TD
    A --> B
    """)
```
# Refs
- [Mermaid中文网](https://mermaid.nodejs.cn/intro/getting-started.html)
