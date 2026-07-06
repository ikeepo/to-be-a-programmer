---
  tags:
    - specificity
---
# Pseudo Classes & Elements
# Pseudo Classes
Pseudo-classes are special CSS keywords that allow you to select an element based on its specific state or position.

The element's state or position could include:

- When it's active.
- When it's being hovered over by a mouse.
- When it's the first child of a parent.
- When it's the last child of a parent.
- When a link has been visited.
- When it's disabled.

```shell
selector:pseudo-class {
  CSS properties
}
```

## User Action Pseudo-classes
They enable you to change the appearance of elements based on user interactions, improving the overall user experience.

```shell
:hover
:active
:focus
:visited
:focus-within
:enabled
:disabled
:target
```

## Input Pseudo-classes
```shell
:enabled 
:disabled
:checked
:valid
:invalid
:in-range
:out-of-range
:required
:optional
:autofill
```

## Location Pseudo-classes 
```shell
:any-link
:link
:local-link
:visited
:target 
```

## Tree-Structural Pseudo-classes 
```shell
:root
:empty
:nth-child(n)
:nth-last-child(n)
:first-child
:last-child
:only-child
:first-of-type
:last-of-type
:nth-of-type(n)
:only-of-type
```
## Functional Pseudo-classes 
```shell
:is()
:where()
:has()
:not()
```

# Pseudo Classes 
virtual or synthetic elements that don't directly match any actual HTML elements.

```shell
selector::pseudo-element {
  property: value;
}
```

```shell
::before
::after
::first-letter
::marker
::placeholder
::spelling-error
::selection
```


# specificity
Think of CSS specificity as a weighting system or a "score" that browsers use to decide which style wins when multiple rules try to change the exact same element.

Specificity is calculated using three distinct columns (or buckets): [ IDs , Classes , Elements ].

```shell
/* Score: [ 0, 1, 0 ] (1 class) */
.highlight { color: blue; }

/* Score: [ 0, 0, 1 ] (1 element) */
p { color: red; }
```
