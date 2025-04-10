# Rust

## Principles
1. There's no concept of uninitialized or null values for fiels unless explicitly wrapped in an Option.
2. A variable can only directly call methods that are defined for its type.

## Concepts
### data type
##### `usize vs i32`
usize mean unsigned (>=0), it's pointer sized.
### [generic parameters](https://doc.rust-lang.org/reference/items/generics.html)
`<U,F>` types involved in the method. not all types rather only the additional types introduced by the method that need to be determined by the caller or inferred by the compiler.
The order doesn't inherently matter.
- pointer-sized
`usize` and `isize` are called pointer-sized integers because their size matches the CPU's native pointer size.
**pointer-size** means architecture-dependent.
A pointer(memory address) must be able to reference any location inmemory.
Vec, arrays and slices use `usize` for indexing because memory addresses are pointer-sized, and indexing is essentially pointer arithmetic.
If you're serializing data to disk or sending it over a network, avoid `usize` because its size varies across platform.
When it refers the memory location, you should use `usize`;
##### Vec indexing
direct indexing (`v[index]`) returns the value, explicit reference `&v[index]` returns a borrow.
`v[index]` computes the memory offset as $let offset = index * std::mem::size_if::<T>();$, this is why `usize` is used for indexing.

##### linked list

##### Box<T> is a smart pointer that owns a value of type T on the heap
It's pointer in the sense that it holds the memory address of the heap-allocated data, but it's more than a raw pointer because it manages ownership and cleanup.
You can take `Box<T>` as a single-owner handle to the heap data.

`&Box` arises when you want to **borrow** the Box without taking ownership.
`&Box<T>` is a reference to the `Box` itself, not directly to the `T` inside it.
##### `&mut Option<Box>. as_ref => Option<&Box>`
`as_ref()` abstracts over the reference type (whether it's `&Optuon<T>` or `&mut Option<T>`), producing an Option containing a reference to the inner value (T). The mutability of the origianl reference doesn't carry through to the result - it always give an immutable borrow;
`r` is `&mut Option<Box>` ,so `*r` will get `Option<Box>` which don't have `val` field, the `as_ref` convert `Option<Box> or &mut Option<Box>` into `Option<&Box>` which give you access to `val` field.
### binding vs type
`mut` is part of the binding , not the type.
It reflects how mutability is handled in the language.
Mutability is a Property of the Binding, not the Type.
`mut` indicates that the variable binding is mutable, meaning you can modify the value it holds.
The type describes what the variable holds, not how it can be used.
### `as_mut vs as_ref`
- `Option<T>::as_ref(&self) -> Option<&T>`
Borrows the inner value of an `Option` immutably, returning an Option containing an immutable reference to the inner value.
- `Option<T>::as_mut(&mut self) -> Option<&mut T>`
Borrows the inner value of an Option mutably, returning an Option containing an mutable reference to the inner value.
`&mut self` requires a mutable reference to the Option;
`as_mut` is a mutable version of `as_ref`;
### confusion about `=`
Assigning a value versus Assigning a pointer or a reference.
```
let mut r = &mut list1;
r = &mut r.as_mut()?.next;
```
r is a mutable reference, not assigning the `&mut list1` to r, it's mutably bind r to the reference of list1, then not assigning again, but bind r to the &mut value which is `r.as_mut()?.next` where `r.as_mut()` work because r is &mut which is required by `.as_mut(&mut self)`, then get the `Box` which is a smart pointer by `?`, then you can access the `next` variable.
The reference or pointer is a moving point, rather a location waiting assigned which is the mechanism of data assignment in common programming.
### `T` is not a keyword, just a convention
A placeholder name used to represent a generic type.
It's part of Rust's generics system.
```
fn print_type<T>(value: T) {
    println!("Type of value: {}", type_name::<T>());
}
```
