# cargo
## change resource
> [1](https://rustwiki.org/zh-CN/cargo/reference/source-replacement.html)
```shell
# ~/.cargo/config

[source]
[source.crates-io]
registry = "https://github.com/rust-lang/crates.io-index"
replace-with = "ustc"
# 中科大
[source.ustc]
registry = "https://mirrors.ustc.edu.cn/crates.io-index"
# 上海交通大学
[source.sjtu]
registry = "https://mirrors.sjtug.sjtu.edu.cn/git/crates.io-index/"

# 清华大学
[source.tuna]
registry = "https://mirrors.tuna.tsinghua.edu.cn/git/crates.io-index.git"

# rustcc社区
[source.rustcc]
registry = "https://code.aliyun.com/rustcc/crates.io-index.git"
# Subcommand
## [`cargo-readme`](https://crates.io/crates/cargo-readme)
```shell
cargo install cargo-readme
cargo readme > README.md
```
优先使用`lib.rs`内容，没有会使用`main.rs`;
