# Variables
# Concepts
- variable syntax, traditional way to define variables:
  
```shell
:root {
  --main-color: #3498db;
}
var(--main-color,  fallback_value)
```

- `@property` syntax, more fancy way to define variables:

```shell
@property --property-name {
  syntax: '<type>'; <color>, <length>, <number>, <percentage>
  inherits: true | false;
  initial-value: <value>;
}
```
