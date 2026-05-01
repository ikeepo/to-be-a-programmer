# Setup

# Question
## What `Follow Rust 2024 edition best practices` mean?
<[The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/)> 会列出所有变换。如何实现：

- Cargo.toml中声明

```shell
[package]
edition = "2024"
```

- `cargo clippy`

```shell
cargo clippy -- -D warnings # 将所有建议视为错误，强迫在编写阶段就遵循最高标准
```

- `cargo fix --edition`

[last gemini](https://gemini.google.com/share/e2691f5e6c9d)
