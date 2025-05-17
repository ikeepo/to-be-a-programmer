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
## Ownership
涉及变量移动，就要考虑ownership;
## Memory Perspective
从内存角度思考代码，也就是从type角度进行对应，也就是从type角度查看源代码签名；
