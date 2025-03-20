# Add from wle need to relative or absolute path
```shell
portry add file.whl  # wrong
poetry add ./file.whl # right
```
# How to Migrate from venv to poetry

### pipx

推荐使用pipx安装poetry，但是pipx必须绑定某个python使用，因此绑定全局的python，同时将poetry通过全局的python下的
全局pipx安装，也就是得到全局的poetry。

### 修改源

##### 全局

```shell
poetry config repositories.pypi https://pypi.tuna.tsinghua.edu.cn/simple
poetry config --list
poetry config unset repositories.pypi # 恢复
```

##### 仅修改当前项目

```toml
[[tool.poetry.source]]
name = "tsinghua"
url = "https://pypi.tuna.tsinghua.edu.cn/simple"
priority = "default"

[[tool.poetry.source]]
name = "pypi"
url = "https://pypi.org/simple"
priority = "supplemental"
```

# 从requirements.txt安装

poetry 本身不支持，只能逐个安装;

```shell
cat requirements.txt | xargs poetry add
```

# 如何在新的路径下使用旧的环境

> [docs-managing environments](https://python-poetry.org/docs/managing-environments/#fish)

```shell
poetry init # 创建新环境
poetry config virtualenvs.path # 找到并进入环境所在路径
# delete 新环境
# rename 旧环境 为新环境名称
```
# 根据pyproject.yaml修改poetry.lock
`poetry lock`
# `poetry show module`依据`poetry.lock`

# `$VIRTUAL_ENV`环境变量可能影响使用的环境
`unset VIRTUAL_ENV`清除，这个貌似是每个poetry项目单独的
# Refs

1. [Migrating a Project to Poetry](https://browniebroke.com/blog/2020-10-18-migrating-project-to-poetry/)
2. [the pyproject.tomal file](https://python-poetry.org/docs/pyproject/)
3. [how to import an existing requirements.txt into a Poetry project](https://stackoverflow.com/questions/62764148/how-to-import-an-existing-requirements-txt-into-a-poetry-project)
