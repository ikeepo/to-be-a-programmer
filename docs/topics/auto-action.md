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
