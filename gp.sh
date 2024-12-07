#!/bin/bash

# 获取当前仓库的远程仓库名称（假设使用的是第一个远程仓库，通常是 'origin'）
remote_name=$(git remote)

# 获取远程仓库 URL（可选，用于调试或验证）
remote_url=$(git remote get-url $remote_name)

# 如果没有提供提交消息，则使用默认消息
message=${1:-"u"}

# 添加所有更改
git add .

# 提交更改，使用提供的提交消息
git commit -m "$message"

# 推送更改到提取的远程仓库和 master 分支
git push -u $remote_name master

