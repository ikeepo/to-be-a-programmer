#!/bin/bash

# 获取当前仓库的远程仓库名称（假设使用的是第一个远程仓库，通常是 'origin'）
remote_name=$(git remote)

# 获取远程仓库 URL（可选，用于调试或验证）
remote_url=$(git remote get-url $remote_name)

# 获取本机电脑型号（适用于 Windows 和 Linux）
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux 系统
    computer_model=$(hostnamectl | grep "Model" | awk -F: '{print $2}' | xargs | cut -c 1-10)
    if [ -z "$computer_model" ]; then
        # 如果hostnamectl命令不可用，可以尝试使用 lscpu 命令
        computer_model=$(lscpu | grep "Model name" | awk -F: '{print $2}' | xargs | cut -c 1-10)
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS 系统
    computer_model=$(system_profiler SPHardwareDataType | grep "Model Name" | awk -F: '{print $2}' | xargs)
else
    # Windows 系统
    computer_model=$(wmic computersystem get model | sed -n '2p' | cut -c 1-10)
fi

# 弹出输入框让用户手动输入提交消息
echo "请输入提交消息："
read message

# 将电脑型号添加到提交消息中
commit_message="$message"

# 添加所有更改
git add .

# 提交更改，使用提供的提交消息
git commit -m "$commit_message"

# 推送更改到提取的远程仓库和当前分支
git push -u $remote_name $(git rev-parse --abbrev-ref HEAD)

# 重新拉取数据，因为github workflow会更新README
sleep 30s
git pull
