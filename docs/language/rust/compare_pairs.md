# Compare Pairs
## `Option.as_mut` vs `RefCall.borrow_mut`

- `outer mutability &mut` vs `interior mutability &`
- Compile-time vs Runtime  for Borrow Rules


## `Option::map` vs `Option::unwrap()`
`map` handle both Some and None, avoids explicit unwrapping,reducing the risk of panics and making code more declarative.
There are two flavors of map in Rust, one for iterator map (many values), one for Option tranformed.
`map` follow a functional programming pattern: take a container, apply a transformation to its concents, and return a new container of the same kind.
