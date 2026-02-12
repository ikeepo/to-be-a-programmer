# CSS
## Concepts

- While HTML defines the structure and {{}}  <option value="content">content</option>
  <option value="undefined">undefined</option>
</select> of a webpage, CSS is used to add style, JavaScript makes your webpage <select onchange="this.style.backgroundColor = (this.value == 'interactive' ? 'transparent' : '#ffcccc');" style="border: none; border-bottom: 2px solid gray; font-weight: bold; padding: 2px; cursor: pointer;">
  <option value="">???</option>
  <option value="interactive">interactive</option>
  <option value="undefined">undefined</option>
</select>

- CSS works by selecting HTML elements and applying styles to them.

- One of the most powerful aspects of CSS is its ability to create responsive designs. CSS allows you to adjust layouts, font sizes, and other visual elements based on the screen size of the device viewing the website.

- Another important feature of CSS is its cascading nature, which is where the "cascading" in its name comes from.This means that styles can be inherited and overridden, allowing for a hierarchical structure of styling.

- A CSS rule is made up of two main parts: a selector and a declaration block.

- All id selectors must start with a hash # symbol.

- All class selectors must start with a dot .

- CSS can be applied to a webpage in three main ways: inline, internal, or external.

- A descendant combinator is used to target elements matched by the second selector if they are nested within an ancestor element that matches the first selector. An ancestor can be a parent element or a parent's parent.

- The child combinator (`>`) in CSS is used to select elements that are direct children of a specified parent element.

- The next-sibling combinator (`+`) in CSS selects an element that immediately follows a specified sibling element.

- The subsequent-sibling combinator (~) in CSS selects all siblings of a specified element that come after it.

- Block-level elements behave like large containers or "blocks" that take up the full width of their parent container. They always start on a new line, and their height and width can be adjusted.

- Inline elements only take up as much space as they need. They flow within the surrounding content and do not break onto a new line.

-  inline elements cannot have their size controlled, whereas inline-block elements allow for full control over dimensions while still staying inline with other content.

- Margins control the space outside an element, while padding controls the space inside an element

- If three values are provided, the first value applies to the top margin, the second value to the left and right margin, and the third value to the bottom margin.

- If four, top-right-bottom-left.

# Questions

- Why does the space between two elements affect the layout?

The browser doesn't delete all spaces, but compresses consecutive spaces (including line breaks and tabs) into one 'space character'.

-


# Boilerplate
```shell
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
