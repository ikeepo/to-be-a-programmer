# [std::boxed](https://doc.rust-lang.org/std/boxed/struct.Box.html)
```rust
pub struct Box<T, A=Global>(/*private fields*/)
where
  A: Allocator,
  T: ?Sized;
```
A pointer type uniquely owns a heap allocation of type T.
It provides the simplest form of heap allocation in Rust. Boxes also ensure that they never allocate more than `isize::MAX` bytes.

# `Box` vs `Rc`
`Box` provides exclusive ownership of the data on the heap.
Exclusive ownership means that a single variable has complete control over a piece of data at any given time.
# Allocator
`A` is an optional generic parameter representing the allocator used to manage the memory. It defaults to `Global` which is the default global allocator provided by Rust.
`Allocator` is the trait bound on the A parameter.
