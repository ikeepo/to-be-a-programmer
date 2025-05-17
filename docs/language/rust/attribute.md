# Attribute
## `#[inline]`
a hint to the compiler to inline the function.
Inlining is an optimization technique where the compiler replaces a function call with the actual body of the function at the call site.
It can eliminates the overhead of a function call.
[`#[inline]`](https://nnethercote.github.io/perf-book/inlining.html) do not gurantee that a function is inlined or not inlined, it's just a suggestion, the compiler decides whether to inline based on its own heuristics, such as function size, call frequency, and optimization level(`--release` mode).

### Why need inline
The key is function call.
use [compiler explorer](https://rust.godbolt.org/) to understand the underling code.
### When to use `#[inline]`
small but called repeatedly.
- `new`
