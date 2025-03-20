# nvim 是一个事件驱动框架

许多功能是监听事件，然后调用回调函数。

# `setup`是关键字么？

`setup`并不是一个关键字，只是惯例函数名，

1. 不是lua的关键字，你可以随便定义setup函数在lua中
2. 不是nvim的关键字，nvim的核心api，`vim.api`中并未定义setup
   nvim社区约定用setup作为插件的初始化函数，负责配置插件的行为。
3. lazy.nvim可以在opts或者config字段中使用setup()，当配置opts时候，lazy.nvim会自动调用`require('module_name').setup({...})`.

# LazyVim vs lazy.nvim

lazy.nvim是一个插件管理器，LazyVim是一个基于lazy.nvim框架做好的使用demo，官方出品，预配置基本插件，以及如何规范使用lazy.nvim，有点类似更多人分享的自己的dotfiles. 不过是lazy.nvim作者发布的。
lazy.nvim ==> LazyVim ==> dotfiles on github

# `nvim_create_buf({listed}, {scratch})                       *nvim_create_buf()*`

`{listed}` 中`{}`并不表示表格，这个语境是文档，文档中用`{}`区分签名中是参数名还是普通文本。
`{}`包裹参数名表示这些是named arguments（伪，lua本身不支持named arguments,lua是纯位置参数语言）.
named arguments又称为关键字参数，同生态的除了位置参数，还有table of options, lua经常使用单个table传参数，用table的键值对模拟命名效果。
listed 在这里只是文档中的惯例，用于表示是一个bool，改成什么对代码本身没有影响，只是在文档层面的命名。
nvim的底层是C，会检查类型，lua不会，lua没有强制类型要求，只负责传递。

# `vim.api`

这是nvim内置的用[C实现的API](https://github.com/neovim/neovim/tree/master/src/nvim/api)，暴露给Lua使用。让Lua能够操作Nvim的内部功能。
nvim启动时候，vim.api被注入到Lua的全局明明空加你`vim`。所以在`.lua`代码中可以直接调用。

# 嵌入nvim的lua5.1跟linux `apt install lua5.1`有什么区别

nvim内嵌的是5.1，而不是最新版本，为了能够配合使用luajt，lua5.3跟5.1改动很大，这是nvim文档中介绍的。
内嵌的lua5.1有标准库，但不是全部功能，限制了io和os，放置脚本直接访问文件系统。具体使用的是LuaJIT比普通lua多了bit模块和JIT优化。nvim装的是LuaJIT2.1,只是兼容Lua5.1，并非标准Lua5.1.
所以，常谈到的nvim插件，其实是lua包，类似python通过pip安装包一样，nvim嵌入的是lua，通过lazy.nvim安装扩展plugins.

# Debug

通过continue启动debug，默认为运行脚本所在路径为cdw，

# 不显示中文

OS level question, rather nvim.

# Poetry

### How to activate the poetry virtual enviriment in nvim

```shell
poetry run nvim name.py
```

# Plugin

## plugin creation dir layout

```shell
├── LICENSE
├── plugin  # get executed as soon as nvim starts, like keymaps or autocmds
│  └── plugin-file.lua
├── lua # major of the functionality, work until user explicitly `require('name')`
│  └── main-file.lua
└── README.md
```


# how to search function docs
```shell
# in nvim
:Telescope help_tags
# the cmd want to know
```
# LSP vs Pyright
LSP 是一个通信协议，专门定义编辑器nvim与语言服务器pyright之间的通信规则，如果输入gx命令，编辑器将向pyright发送一个通讯请求，pyright分析后返回变量定义位置，编辑器便会跳转到对应位置。
### nvim-lspconfig
封装了lsp配置复杂度，实现简单配置开箱即用；
# Refs

1. [NeuralNine](https://www.youtube.com/watch?v=tfC1i32eW3A)
2. [DevOps Toolbox](https://www.youtube.com/watch?v=RziPWdTzSV8)
3. [TJ DeVries](https://www.youtube.com/watch?v=lyNfnI-B640)
4. [nvim-dap](https://github.com/mfussenegger/nvim-dap)
5. [流程](https://www.youtube.com/watch?v=lEMZnrC-ST4)
6. [How to write a neovim plugin in lua](https://miguelcrespo.co/posts/how-to-write-a-neovim-plugin-in-lua)
7. [nvim -best practices](https://github.com/nvim-neorocks/nvim-best-practices)
