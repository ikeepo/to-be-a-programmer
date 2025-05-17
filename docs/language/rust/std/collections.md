# [`std::collections`](https://doc.rust-lang.org/std/collections/index.html)

## [Struct VecDeque](https://doc.rust-lang.org/std/collections/struct.VecDeque.html)
A double-ended queue implemented with a growable ring buffer.
- [ring buffer:circular buffer]()
When you reach the end of the array, the next position wraps around to the start (index 0) which makes a loop, making it resemble a ring.
## [`Struct HashMap`](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

## [`Enum Entry`](https://doc.rust-lang.org/std/collections/hash_map/enum.Entry.html)
```rust
use std::collections::HashMap;
fn main() {
  let mut letters = HashMap::new();
  for ch in "s gad ga".chars() {
    let y = letters.entry(ch).and_modify(|x| *x += 1).or_insert(1);
    println!("{}", y);
  }
}
```
