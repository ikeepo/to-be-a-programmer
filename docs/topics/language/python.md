# pyenv

## shims 机制

`which python` 得到的总是`/home/zoe/.pyenv/shims/python`, 不管实际切换使用的是哪个版本的python。
原因如下：

1. which python返回的是PATH下找到的第一个python
2. pyenv将shims/python排在第一位，提供切换后的版本

- shim原意垫片、薄片
  指代轻量级夹层，适配层；
- shims不是软连接，是脚本的动态转发
  `/.pyenv/shims/python`是一个固定的shell脚本,内容如下：

```shell
#!/usr/bin/env bash
set -e
[ -n "$PYENV_DEBUG" ] && set -x

program="${0##*/}"

export PYENV_ROOT="/home/zoe/.pyenv"
exec "/home/zoe/.pyenv/libexec/pyenv" exec "$program" "$@"

```

动态转发不会生成新的文件，而软连接会增加新文件的出现。
这个不经意间涉及到了Linux跟Windows的差异，Windows是静态管理，会生成很多残留文件，导致久用臃肿。
这可能是其中一个差异点。
