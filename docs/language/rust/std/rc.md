# `std::rc::Rc`
A single-threaded reference-counting pointer.
Reference Counted.
The inherent methods of `Rc` are all associated functions, which means you have to call them as **e.g.**, `Rc::get_mut(&mut value)` instead of `value.get_mut()`. This avoids conflicts with methods of the inner type `T`;
## Decode
##### what single-threaded mean and opposite
It means the Rc pointer is intended for use in an environment where only one thread accesses and manipulates it at a time.
For multi-threaded is `Arc` which stands for "Atomically Reference Counted";
##### Reference Counted Pointer
##### What is associated functions
Functions that are tied to a type rather than to an instance of that type.
They are defined in an `impl` block for the type and don't take `self` as a parameter (unlike method);
# Code Explain
## `get_mut`
```rust
use std::rc::Rc;
fn main() {
  let mut x = Rc::new(3);
  *Rc::get_mut(&mut x) = 5;
  assert_eq!(x, Rc::new(5));
}
```
## How to use
```rust
use std::rc::Rc;
fn main() {
    let mut x = Rc::new(3);
    assert_eq!(x, Rc::new(3));
    let y = &mut x;
    *y = Rc::new(5);
    assert_eq!(*x, 5);
}
```
- `Rc & Refcell` why the `borrow_mut` method belones to RefCell rather Rc?
```rust
pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option {
  root.map(|node| {
    node.borrwo_mut().swap_all();
    node
  })
}
```
Here is the concept [`automatic dereferencing`](/docs/topics/language/rust/general.md#here-is-the-concept-automatic-dereferencinghttpsdocrust-langorgreferenceexpressionsfield-exprhtmlhighlightautomatic20dereferencedr-exprfieldautoref-deref);
The `node ` is "Container Operand". The container is because it encapsulates or pointers to the actual data of interest, often requiring dereferencing to reach that data.
`borrow_mut` is th `field`.
Autoderef is Rust's process of automatically dereferencing a container operand (by `Deref` or `DerefMut`) as many times as needed to make a filed access or method call valid.


# Why need Rc rather direct &
`&` only has one oewner, and `Rc` can create multi owners.
Reference is tied to the lifetime of the original vairbale, if the owner goes out of scope, the reference is invalid.  `Rc` the data lives as long as any `Rc` reference exists, decoupling it from the original scope.
# The data `Rc` managed is always allocated on the heap
# `Weak<T>` Weak reference
A weak reference in Rust is a non-owning reference to data managed by an Rc
# Memory Layout
