# Declaration and Binding
`let mut x = Rc::new(3);`
`let` declares a new variable named `x`, declaration is when you introduce a new variable into the scope.
binding is the process of associating that variable name with a value. for example `=`;
`mut` specifies that the binding is mutable.
# RHS Access Fields or Values
When the variable is on the right, it means the underlying data.
# LHS updates ownership
When assign to a variable on the left, you're changing what these variables hold, not only about data, but also ownership.
## `l = r`
move the value in `r` to `l`;
