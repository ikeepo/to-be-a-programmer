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

```shell
Alignment is how the elements are placed in relation to one another.
Alignment is the process of arranging text and images in a way that creates a visual connection between elements.
- left alignment
- center alignment
- right alignment
- justified alignment: text is aligned to both the left and right margins
- vertical alignment

```

- Composition

`Composition is the art of arranging elements to create a harmonious design. `

- Balance

`Balance is how the visual weight is distributed within a composition. `

- Hierarchy 

`Hierarchy establishes the order of importance of the elements in a design. `

- Contrast 

`Contrast is helpful for guiding user attention to what you want to emphasize.`

```shell
Web Content Accessibility Guidelines, or WCAG standards:
1. Text with a contrast ratio of 7:1 is considered the AAA standard
2. Text with a contrast ratio of 4.5:1 is considered the AA standard

What impacts the contrast ratio: Hue, Saturation, Lightness
```
How to know the contrast? The developer tools --> style --> color / [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)


- White/Negative Space

`The empty space in a design. It's the area surrounding the elements.`
```shell
- Macro white space is the space between larger elements like images, text blocks, and buttons.
- Active white space is the space that is intentionally created to help guide the user's eye and draw attention to certain elements on the page.
- Micro white space is the space between individual characters in a line of text.
```

> Law of Proximity: elements that are close together are perceived as being related, while elements that are far apart are perceived as being unrelated

- UI & UX 

`user interface, user experience. An application with a well-designed user experience is intuitive, easy to use, efficient, accessible, and enjoyable.`  

```shell
# Image 
- Responsive images 
- resolution for images
- size of your images
- image placement: balance, hierarchy, and alignment
- accessibility for images
```

- scale 

`The "scale" of something refers to its size. When you're looking at scaling in your web design, you're looking at the size relationships between different elements, and how these elements might adapt to different screen sizes.`

- Progressive Enhancement
`Progressive enhancement is a design approach that ensures all users, regardless of browser or device, can access the essential content and functionality of an application.`
```shell
- All core content and basic functionality should be accessible on all browsers
- All advanced layouts should be provided through external CSS stylesheets
- All advanced functionality should be provided through external JavaScript files
- A user's browser preferences should be respected
```


## User-Centered Design
- One of the first aspects of user-centered design is considering your target demographics


- Another aspect to consider is the goal of your end users. 

- Ultimately, user-centered design means you need to put the user at the forefront of your decision making

### User Research
- Net Promoter Score, or NPS. The NPS measures how likely your users are to recommend your product to a friend.

- Exit interview

- User testing: AB test 

- user requirements refer to the stories or rubric that your application needs to follow

### Dark Mode
- The first consideration is the avoidance of saturated colors in dark mode. Saturated colors are colors that are bright and intense

- Another consideration with dark mode is the use of pure black backgrounds with white text

- Another consideration is the use of dark mode with the site's brand identity.

### Breadcrumbs
`Breadcrumbs are a navigation aid that shows the user where they are in the site's hierarchy`

- Common **separators** include the greater than sign (`>`), right angle quotation marks (`»`) ,and the forward slash (`/`).

- **Position**: Breadcrumbs are typically placed at the top of the page, either above or below the main navigation bar

- **Size**: You want to make sure the breadcrumbs are large enough to be easily read, but not so large that they take up too much space on the page.

### Designing Cards 
- The first consideration for card design should be simplicity.

- Having less information and good spacing between items on the card makes it easier for the user to process the information

- Another thing to consider is where the user can click on the card.

- Another consideration is the use of media on your cards.

- One of the last things to consider is the use of color hierarchy

### Designing Infinite Scrolls 
`Infinite scrolling is a design pattern that loads more content as the user scrolls down the page. `

- Infinite scrolling is also used as a substitute for pagination

- "Load More"

-  "Back" button

### Designing Modal Dialogs 
`A modal is the type of pop-up that a website might show you on top of their content.`

- The content behind a modal is usually dimmed.

- It's always a good idea to allow the user to click outside of the modal to close it.

- You'll often see very prominent buttons on modals. These are called CTAs, or call-to-action. 

- Modals should also have a close button. 

### Progress Indication
`Progress indication is a way to show users how far they are in a process. `

- The first consideration is to keep it simple.

- The second consideration is to make it possible to go back to previous steps. 

- Another consideration is to make the progress indication section easy to find. 

- The last consideration is to have clear section titles, percentages, or steps.

### Designing Shopping Carts

- The first design consideration is making sure the shopping cart is visible to users at all times. 

- Another consideration is providing a clear way for users to update the quantity of items in their cart. 

- You should also provide a "Remove" button next to each item in the cart. 

- Another consideration is the shopping cart icon itself. The icon should be something easily recognizable for all users.

- When the user wants to review the total in their cart, they should be able to easily find the total cost of all items in the cart. 

- Finally, you should provide a clear call-to-action button for users to proceed to checkout.

### Progressive Disclosure

`A progressive disclosure is a design pattern used to only show users relevant content based on their current activity and hide the rest. `

- The first consideration is to keep all important information visible at all times. 

- Another consideration is to provide a single access point for users to access additional features or information. 

### Lazy registration

```shell
Lazy registration is a UI design pattern that allows users to browse and interact with your application without having to register.
Lazy registration is a useful design pattern that allows users to see the value of your application before they are willing to provide their information.
```


