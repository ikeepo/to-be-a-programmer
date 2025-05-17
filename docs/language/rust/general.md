# Rust
## Practice Materials
- [Grind 75](https://www.techinterviewhandbook.org/grind75/)

## Principles
1. There's no concept of uninitialized or null values for fiels unless explicitly wrapped in an Option.
2. A variable can only directly call methods that are defined for its type.

## Concepts
### Documentation comments`//!`
The comments are processed by `rustdoc` to generate API documentation.
Document the containing item, like a module, crate or file.
### Inner documentation comments `///`
Document the next item
### `O(log n)`
Certain divide-and-conquer algorithms, such as binary search;

### data type
##### `usize vs i32`
usize mean unsigned (>=0), it's pointer sized.
### [generic parameters: generic type](https://doc.rust-lang.org/reference/items/generics.html)
`<U,F>` types involved in the method. not all types rather only the additional types introduced by the method that need to be determined by the caller or inferred by the compiler.
The order doesn't inherently matter.
### [generic function](https://doc.rust-lang.org/rust-by-example/generics.html)


### [type parameter]()

### [move](https://doc.rust-lang.org/rust-by-example/scope/move.html)

```rust
let x = 1;
func(x);
println!("{}",x) // wrong, because the ownership of resource is transferred to func, which is called move
```
### variable is a memory location with offset which inclued structure
A variable in Rust is a named binding that associated an identifier with a value stored in memory.
A type determines its size, layout, and interpretation.
Each piece of memory has exactly one owner at a time.
When a variable owns data, it's responsible for freeing that memory when it goes out scope (drop mechnism)
### Here is the concept [`automatic dereferencing`](https://doc.rust-lang.org/reference/expressions/field-expr.html?highlight=automatic%20dereferenced#r-expr.field.autoref-deref)
Also called [autoderef](/docs/topics/language/rust/std/rc.md#how-to-use) .
### [Interior Mutability](https://doc.rust-lang.org/reference/interior-mutability.html)
[it's](https://doc.rust-lang.org/reference/interior-mutability.html) a design pattern in Rust that allows you to mutate data ven when there are immutable references to that data.
This action is not allowed by the borrowing rules.


### pointer-sized
`usize` and `isize` are called pointer-sized integers because their size matches the CPU's native pointer size.
**pointer-size** means architecture-dependent.
A pointer(memory address) must be able to reference any location inmemory.
Vec, arrays and slices use `usize` for indexing because memory addresses are pointer-sized, and indexing is essentially pointer arithmetic.
If you're serializing data to disk or sending it over a network, avoid `usize` because its size varies across platform.
When it refers the memory location, you should use `usize`;
##### linked list

##### Box<T> is a smart pointer that owns a value of type T on the heap
It's pointer in the sense that it holds the memory address of the heap-allocated data, but it's more than a raw pointer because it manages ownership and cleanup.
You can take `Box<T>` as a single-owner handle to the heap data.

`&Box` arises when you want to **borrow** the Box without taking ownership.
`&Box<T>` is a reference to the `Box` itself, not directly to the `T` inside it.
### binding vs type
`mut` is part of the binding , not the type.
It reflects how mutability is handled in the language.
Mutability is a Property of the Binding, not the Type.
`mut` indicates that the variable binding is mutable, meaning you can modify the value it holds.
The type describes what the variable holds, not how it can be used.
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
# Perspective
## Data Structure
- [Visualizing memory layout of Rust's data types](https://www.youtube.com/watch?v=7_o-YRxf_cc)

## variable
```rust
let x  = vec![1,2,3]
```
`123` is on heap, Vec is on stack with ptr+len+cap, `x` is the name bound to the Vec structure.
`x` isn't another memory location, it's the Vec strucure itself. When you use `x`, Rust accesses that stack memory directly.
## Compile-time
`x` is a compile-time name that the Rust compiler uses to refer to a specific piece of data.
Once the code is compiled to machie code , `x` disappears as a label and becomes an offset or regiter reference to actual memory location of the Vec structure.
So, at runtime, on the memory level, `x` doesn't exist as a separate entiry.
Compilation is indeed the process of transforming symbolic representations like variable names into concrete instructions that operate on memory locations or registers in the final execuable.
