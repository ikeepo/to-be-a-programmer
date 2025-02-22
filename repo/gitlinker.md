# [gitlinker.nvim](https://github.com/linrongbin16/gitlinker.nvim?tab=readme-ov-file#break-changes--updates)

## blame support

git中的一个命令，[`git blame`](https://git-scm.com/docs/git-blame)显示文件中每一行是由谁在哪个提交中修改的。

## git blame view

github上的网页界面，专门用于展示文件的blame信息。

## full [git protocols](https://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols) support

git protocols是针对git本地和远程仓库之间传输数据这个场景需要的。git里面有多个协议，比如gitlab repo中clone项目时候一般有两个选项：`https` and `ssh`，这就是两个协议。还有`local protocol` and `git protocol`两个协议。

## Respect ssh host alias.

Which means it can interpret and use SSH host aliases defined in the user's SSH configuration file (`~/.ssh/config`)

- SSH Host Aliases
  配置在config文件中，以更快捷的实现`ssh alias_name` rather `ssh name@host -p -i `, just simple shortcut for a long defination.

## ?plain=1

github for view MD files in their raw.

## Use git stderr output as error message.

- `2>&1`  
  shell中将stderr转给stdout,12表示文件描述符，这是shell的默认分配，0是stdin。
  > 这里git stderr并不是一个专门的stderr，就是指shell的stderr
- `&` 表示引用文件描述符

## wslview

wsl utilities 的一部分。（竟然有这么好的工具，孤陋寡闻）
