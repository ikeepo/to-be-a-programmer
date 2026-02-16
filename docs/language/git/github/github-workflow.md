# Github Workflow
## Refs 
- [Syntax](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#jobsjob_idsteps)
- [Use cases and examples](https://docs.github.com/en/actions/use-cases-and-examples)
- 如何保留workflow文件但是不执行？

手动从github网页Actions中disable

## Terminology
### permissions
- 谁在哪里的权限？

Github Actions 运行时自动生成GITHUB_TOKEN（每一次任务的每一次执行单独生成Per Execution）,这个GITHUB_TOKEN需要有写入权限才能执行代码修改任务；



## Plugins 
### [actions-poetry](https://github.com/marketplace/actions/python-poetry-action)
> [Test a Poetry project with GA](https://jacobian.org/til/github-actions-poetry/)
