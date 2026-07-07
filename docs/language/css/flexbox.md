# Flexbox
# Concepts
- CSS flexbox is a one-dimensional layout model that allows you to arrange elements in rows and columns within a container:

    - flex container: an HTML element with a flex layout. apply `display: flex` to an element to make it a flex container

    - flex item:  the direct children of a flex container.

- Every flex container has two axes:
    
    1. The main axis.(horizontal), defined by flex-direction

    2. The cross axis.(vertical)

- flex properties:
  
    1. `flex-direction: row(default), row-reverse, column, column-reverse`

    2. `justify-content: flex-start flex-end center space-between space-around space-evenly` aligns the child elements along the main axis of the flex container.

    3. `align-items: stretch` distribute the child elements along the cross axis

    4. `flex-wrap: nowrap, wrap( allow the items to wrap to the next row or column), wrap-reverse`

    5. `flex-flow: column wrap-reverse;` shorthand property for `flex-direction` and `flex-wrap`

    6. `align-self: ` individual flex item

    7. `order: 0( they appear in the order they're written in the HTML, Items with lower order values appear first)`

    8. `flex-grow: 0|1|2...` how much a flex item should grow relative to the rest of the flex items if there is extra space available inside the parent flex container.

    9. `flex-shrink` It dictates how much a flex item should shrink relative to the other flex items when there isn't enough space inside the parent flex container.
