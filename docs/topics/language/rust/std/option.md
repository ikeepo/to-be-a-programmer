# [`std::option`](https://doc.rust-lang.org/std/option/enum.Option.html)
# `Enum Option`
## [map](https://doc.rust-lang.org/std/option/enum.Option.html#method.map)
```rust
pub fn map<U, F>(self, f: F) -> Option<U>
where
  F: FnOnce(T) -> U,
```
