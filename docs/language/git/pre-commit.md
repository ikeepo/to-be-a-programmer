# [pre-commit](https://pre-commit.com/)

## pre-commit的自动修复流程
```shell
1. 如果发现未staged的内容会自动git stash暂存(在pre-commit运行初识只进行一次全局stash)
2. 运行自动修复
3. git stash pop 拿出暂存的环节
4. 发现与修改后内容有差异，rolling back fixes
# 这个问题出现，是因为pre-commit自动修复的部分，不会自动git add，运行一次pre-commit完成自动修改，再次运行pre-commit此时文件内容是修复后的与之前git add的未修复内容出现冲突，所以会自动git stash修复内容，仓库内容再次成为git add之后的未修复内容，再次发生pre-commit自动修复？但此时自动修复后的内容不就是跟git stash的内容一样么？(这个暂时没解决)
# 想要查看哪些内容修改： git status ;  git diff
```
## pre-commit Best Practice
```shell
为避免上述问题，pre-commit的best practice不是等git commit被动调动，而是pre-commit run --all-files(从.git根目录开始recursively check all files)
```
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
# 配合ruff
pre-commit-config中的args定义是传递给pre-commit使用，是pre-commit的工作流程，不是ruff的配置；
而pyproject.toml中ruff的配置，是配置ruff的运行规则；
# Error
## `[WARNING] Unstaged files detected.`


# pre-commit执行工作流
- pre-commit在本地执行
执行的工作本质也可以放在github action这样的云端
- pre-commit为每个hooks创建虚拟环境
不使用工作目录环境里的配置，而是自己重新创建，放在~/.cache/pre-commit/中；
- pre-commit默认只检staged files(git add 的)
- pre-commit会在运行的当前目录下寻找
如果要在子目录，比如submodule中使用pre-commit，需要显式指定配置文件`--config`;
## 同一个项目里不同submodule里的pre-commit可能会冲突，导致initializing卡住
通过将.pre-commit-config.yaml放置在项目根目录下面，在submoudle中install然后指定--config文件使用pre-commit run，在对应hooks中修改--config参数指定配置文件。
