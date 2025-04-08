# `std::rc::Rc`
A single-threaded reference-counting pointer.
Reference Counted.
The inherent methods of `Rc` are all associated functions, which means you have to call them as **e.g.**, `Rc::get_mut(&mut value)` instead of `value.get_mut()`. This avoids conflicts with methods of the inner type `T`;
## Decode
##### what single-threaded mean and opposite
It means the Rc pointer is intended for use in an environment where only one thread accesses and manipulates it at a time.
For multi-threaded is `Arc` which stands for "Atomically Reference Counted";
##### Reference Counted Pointer
