# [`std::option`](https://doc.rust-lang.org/std/option/enum.Option.html)
# `Enum Option`
## [map](https://doc.rust-lang.org/std/option/enum.Option.html#method.map)
```rust
pub fn map<U, F>(self, f: F) -> Option<U>
where
  F: FnOnce(T) -> U,
```
##### `&mut Option<Box>. as_ref => Option<&Box>`
`as_ref()` abstracts over the reference type (whether it's `&Optuon<T>` or `&mut Option<T>`), producing an Option containing a reference to the inner value (T). The mutability of the origianl reference doesn't carry through to the result - it always give an immutable borrow;
`r` is `&mut Option<Box>` ,so `*r` will get `Option<Box>` which don't have `val` field, the `as_ref` convert `Option<Box> or &mut Option<Box>` into `Option<&Box>` which give you access to `val` field.
### `as_mut vs as_ref`
- `Option<T>::as_ref(&self) -> Option<&T>`
Borrows the inner value of an `Option` immutably, returning an Option containing an immutable reference to the inner value.
- `Option<T>::as_mut(&mut self) -> Option<&mut T>`
Borrows the inner value of an Option mutably, returning an Option containing an mutable reference to the inner value.
`&mut self` requires a mutable reference to the Option;
`as_mut` is a mutable version of `as_ref`;
