# Grid
# Concepts
- Flexbox is content-first, meaning it adjusts the layout based on the content. Grid, on the other hand, is layout-first, allowing you to create the layout and then place items into it. 

- A {{ddmenu('track')}} is the space between two neighboring grid lines. 

- If you use the **normal** value for the `column-gap` property, then the result will be `0` for *grid layouts* (defined by `display: grid`) and `1em` for `multi-column layouts`(defined by `column-count`).

- `grid-template-columns: minmax(150px, 300px) 1fr;` `1fr` 不是意味着整体被切分成2个fr，后面这个1fr应该跟前面的大小一样？

  - 1fr 并不是“把整体宽度分成 2 份取其 1”，它的精确定义是：“瓜分扣除固定/受限空间后，所‘剩余’的可用空间（Free Space）”。


