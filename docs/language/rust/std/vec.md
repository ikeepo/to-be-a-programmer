# [std::vec](https://doc.rust-lang.org/std/vec/struct.Vec.html#capacity-and-reallocation)
## `Struct Vec`
The capacity of a vector is the amount of space allocated for any future elements that will be added onto the vector.
The length of a vector specifies the number of actual elements within the vector.


##### Vec indexing
direct indexing (`v[index]`) returns the value, explicit reference `&v[index]` returns a borrow.
`v[index]` computes the memory offset as $let offset = index * std::mem::size_if::<T>();$, this is why `usize` is used for indexing.
##### the end of the `Vec` acts as the top (right)
So when say a stack bottom to up, it means left to right.

##### `vec.len() -> usize`
