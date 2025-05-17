# Memory Perspective
Data Structure carry information.
If you don't know data structure, you only know 1/3 of the programming.
# Template
## Fields
## Aspects
The layout of a type is[^1] :

- size

- alignment

- relative offsets of its fields


# Prompt
, explain the memory layout of it with example.

# Perspective
[Fro performance](https://www.reddit.com/r/rust/comments/1jy3h80/how_do_you_think_about_rusts_memory_model/), measure measure, which means `invest early on tools` is a good advice.




# Tools
- [std::mem::size_of](https://doc.rust-lang.org/std/mem/fn.size_of.html)

- [criterion](../tools/criterion.md)

# Refs
- [Visualizing memory management in Rust](https://deepu.tech/memory-management-in-rust/)

[^1]: [Type Layout](https://doc.rust-lang.org/reference/type-layout.html)

[^2]: [How do you think about Rust’s memory model?](https://www.reddit.com/r/rust/comments/1jy3h80/how_do_you_think_about_rusts_memory_model/)
