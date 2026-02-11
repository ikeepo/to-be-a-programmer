# flake8
不支持自动修复，需配合其他工具实现自动修复；
# ruff
支持自动修复的flake8替换；
- 为什么不用.ruff文件
也可以写在.ruff中，不过ruff会默认按照pyproject.toml, ruff.toml, .ruff.toml查找；

- 为什么要写在pyproject.toml中
python在PEP518中定义的标准卑职文件，写在这里便于统一管理；
- [部分命令不支持自动修复：F821, F402等](https://docs.astral.sh/ruff/rules/#pyflakes-f)

# E501有时候black解决不了，ruff-format也解决不了
# 手动修复
部分错误应该手动修复，F841， F821
