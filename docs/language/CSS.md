# CSS
## Property Selecter Tools
- [Can I Use](https://caniuse.com/)

- CSS Peeper


## Concepts

- `em`: 并非一个单词缩写，而是继承自M印刷传统，M宽度正好是字体宽度。`em`具有向上继承特点，`rem` 是root即`<html>`字体大小。如果用于`font-size: 2em`则是向上继承，如果用于其他属性，则是基于当前字体的`font-size`;

- While HTML defines the structure and {{ddmenu('content')}} of a webpage, CSS is used to add style, JavaScript makes your webpage {{ddmenu('interactive')}}

- Cascading Style Sheets (CSS) is a {{ddmenu('markup')}} language used to apply styles to HTML elements.

- CSS works by selecting HTML elements and applying styles to them.

- One of the most powerful aspects of CSS is its ability to create responsive designs. CSS allows you to adjust layouts, font sizes, and other visual elements based on the screen size of the device viewing the website.

- Another important feature of CSS is its cascading nature, which is where the "cascading" in its name comes from.This means that styles can be inherited and overridden, allowing for a hierarchical structure of styling.

- A CSS rule is made up of two main parts: a selector and a declaration block.

- All id selectors must start with a hash # symbol.

- All class selectors must start with a dot .

- CSS can be applied to a webpage in three main ways: inline, internal, or external.

- A descendant combinator `figure img {}` is used to target elements matched by the second selector if they are nested within an ancestor element that matches the first selector. An ancestor can be a parent element or a parent's parent.

- The child combinator (`>`) in CSS is used to select elements that are direct children of a specified parent element.

- The next-sibling combinator (`+`) in CSS selects an element that immediately follows a specified sibling element.
```shell
img + figcaption {}
<figure>
  <img>
  <giccaption>
</figure>
```

- The subsequent-sibling combinator (~) in CSS selects all siblings of a specified element that come after it.

- Block-level elements behave like large containers or "blocks" that take up the full width of their parent container. They always start on a new line, and their height and width can be adjusted.

- Inline elements only take up as much space as they need. They flow within the surrounding content and do not break onto a new line.

-  inline elements cannot have their size controlled, whereas inline-block elements allow for full control over dimensions while still staying inline with other content.

- Margins control the space outside an element, while padding controls the space inside an element

- If three values of margin and padding are provided, the first value applies to the top margin, the second value to the left and right margin, and the third value to the bottom margin.

- If four, top-right-bottom-left.

- CSS {{ddmenu('specificity')}} is a fundamental concept that determines which styles are applied to an element when multiple rules could apply.
```shell
0. !important - overwirte any other, used by following the value
1. inline styles
2. id - #
3.0 Class selectors can be combined with other selectors to create more specific rules. - p.class_value
3. class - .
3.2 type - p
4. attribute - [type="text"]
5. pseudo-classes - ::before
6. universal - asterisk(*)
```

- Specificity values are calculated as a four-part value (a, b, c, d):
```shell
a: Inline styles (1 or 0).
b: Number of ID selectors.
c: Number of class selectors, attribute selectors, and pseudo-classes.
d: Number of type selectors, pseudo-elements, and universal selectors.
```

- A media query is a CSS technique used to apply styles based on the characteristics of the device or viewport, such as its width, height, or orientation.

- The Cascade Algorithm is the process the browser uses to decide which CSS rules to apply when there are multiple styles targeting the same element.
```shell
1. relevance
2. origin and !importance
3. specificity
4. order of appearance (last)
```

- Inheritance is a key concept in CSS that determines how styles are passed down from parent elements to their child elements. For the properties not inherited by default, you can use {{ddmenu('padding: inherit')}} in the child property to implement inheritance.

- The Web Content Accessibility Guidelines (WCAG) recommend a minimum contrast ratio of 4.5:1 for normal text and 3:1 for large text.

- While similar to `border`, `outline` doesn't affect the element's dimensions or layout:

# Questions

- Why does the space between two elements affect the layout?

The browser doesn't delete all spaces, but compresses consecutive spaces (including line breaks and tabs) into one 'space character'.

- `background: radial-gradient(shape size at position, color-stop1, color-stop2, ...)`
```shell
.radial-gradient{
  background: radial-gradient(circle closest-side at center, red, yellow 50%, green); --- 红到黄占据50%比例；圆心是100%red，50%是100%yellow；
  height: 60vh;  ---View Height
}
```
```shell
这个圆画多大算是画完了。边缘触碰以最后一个颜色100%为准，停止之外的是这个颜色的纯色。
The size determines the size of the gradient's ending shape which could be:
1. closest-side, 最近的边 == contain
2. closest-corner, 最近的角
3. farthest-side,
4. farthest-corner, == cover
5. contain,
6. cover.
```
# Boilerplate
```shell
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```


## Design Terminology
- Layout 

`Layout is how the visual elements are arranged on a page or screen to communicate a message. `

- alignment 

`Alignment is how the elements are placed in relation to one another.`

- Composition

`Composition is the art of arranging elements to create a harmonious design. `

- Balance

`Balance is how the visual weight is distributed within a composition. `

- Hierarchy 

`Hierarchy establishes the order of importance of the elements in a design. `

- Contrast 

`Contrast is helpful for guiding user attention to what you want to emphasize.`

- White/Negative Space

`The empty space in a design. It's the area surrounding the elements.`

- UI & UX 

`user interface, user experience. An application with a well-designed user experience is intuitive, easy to use, efficient, accessible, and enjoyable.`  
