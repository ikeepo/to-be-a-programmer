# [RefCell](https://doc.rust-lang.org/std/cell/struct.RefCell.html)
A mutable memory location with dynamically checked borrow rules.
You can have many immutable references or one mutable reference, but not both at the same time. The `RefCell` check this on runtime rather compiler time.
# Concepts
- dynamically checked
Dynamically means it's something happened at runtime.
Statically means it's on the compiler time.
- borrowing
it refers to temporarily using a reference to a memory location without taking owenership of it.
Ownership in here means being responsible for managing that memory.
## Defination
```rust
pub struct RefCell<T>
where
    T: ?Sized,
{ /* private fields */ }
```
##### What the Structure mean
`where` clause in Rust used to specify constraits on generic type parameters.
since it's either sized or unsized, why need here.
The `Sized` is default implemented, so here is relaxing it.
