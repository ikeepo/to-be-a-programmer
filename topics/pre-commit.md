# [pre-commit](https://pre-commit.com/)
## `.pre-commit-config.yaml`定义pre-commit的行为
## `pre-commit sample-config > .pre-commit-config.yaml`
生成模板配置文件
## `pre-commit install`
用于在本地仓库中安装Git hooks，会在.git/hooks/目录下创建一个名为pre-commit的hook script，这个脚本会在每次`git commit`时候触发，执行`.pre-commit-config.yaml`中定义的检查。
没有配置文件也可以install，但git commit时候不触发任何检查，并提醒没有配置文件。
## pre-commit配置文件修改后并不需要更新.git/hooks/pre-commit文件
后者只是一个触发器，会基于配置文件的内容执行
# 配合flake8
pre-commit会默认从运行命令的当前文件夹里寻找.flake8文件；
如果根目录和submodule都需要，可以通过`args: [--config=absoluate_path/.flake8]`
