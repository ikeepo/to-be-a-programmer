# Box Model
# Concepts
- {{ddmenu('Overflow')}} refers to the way elements handle content that exceeds or overflows the size of the containing element

- while the CSS transform property is a powerful tool for creating visually dynamic web designs, it's essential to use it responsibly with accessibility in mind. 

- The CSS box model defines how HTML elements are structured and positioned. In the CSS box model, every element is surrounded by a box. This box consists of four elements: 
    - the content area, 

    - the padding, 

    - the border,
    
    - the margin.

- Margin collapsing occurs when the vertical margins of adjacent elements overlap, resulting in a single margin equal to the larger of the two.

    - only happened on vertical  direction

    - Adjacent Siblings: two vertical margins come into contact with each other, the larger margin wins 

    - Parent and First/Last Child: a parent element and its first or last child.

    - Empty Elements: if an element has no content, padding, or border, its top and bottom margins can collapse into a single margin.


- why margin collapsing happen? margin collapsing happens to make vertical spacing between elements look more natural and consistent, preventing double-spacing.

- When Margins Don't Collapse

    - The elements are styled with display: flex or display: grid.

    - One of the elements has position: absolute or position: fixed.

    - The elements are floated (float: left or right).

    - There is a border or padding separating the margins (especially relevant for parent/child collapsing).

    - The element has overflow set to something other than visible

- The value of the `box-sizing` property is `content-box` by default, but you can choose `border-box` if you need to. 

-  border-box. It's different because the width and height you set include the element's content, padding, and border (but not its margin). Use border-box when you want the element's total size to stay fixed even if padding or borders change — that's often helpful in responsive layouts.

- A {{ddmenu('CSS reset')}} is a stylesheet that removes all or some of the default formatting that web browsers apply to HTML elements.

- There are two main approaches to CSS resets: you can either
    
    1. define custom CSS resets 

    2. use third-party CSS resets: [Normalize.css](https://necolas.github.io/normalize.css/) [sanitize.css](https://csstools.github.io/sanitize.css/)

- The {{ddmenu('CSS filter')}} property is a powerful tool that allows you to apply graphical effects to elements on a web page. It's particularly useful for adjusting the visual presentation of images, backgrounds, values :
    
    - `blur(2px)`: Gaussian

    - `brightness(150%)`

    - `grayscale(100%)`

    - `sepia(50%)`

    - `hue-rotate(90deg)`

    - `contrast(150%)`

    - `invert`

    - `saturate`

- 


