# Html
## Knowledge

- There are many key concepts in HTML, such as {{ddmenu_u('void element', 'attribute', 'boilerplate', 'id', 'class', 'entity', 'Open Graph Protocol', 'replaced element')}}

- There are {{ ddmenu('six', 'five') }} heading elements.

- What's the difference between MarkUp and MarkDown in HTML? 
Markup use tag to define elements, and markdown is a easier and lighter alternative.

- The `rel` attribute is used to specify the relationship between the linked resource and the HTML document. 

- `<!DOCTYPE html>` tells browsers that the document is an {{ddmenu('HTML5')}} document which is the latest version of HTML.

- You will mainly use the {{ddmenu('div')}} element when you want to group HTML elements that will share a set of CSS styles. 

- The {{ddmenu('section')}} element has semantic meaning over the {{ddmenu('div')}} element which is not semantic. Semantics are the meaning of words or phrases in a language. 

- {{ddmenu('Classes')}} are best used when you want to apply a set of styles to many elements. If you want to target a specific element, it is best to use id because those values need to be unique.

- An HTML entity, or character reference, is a set of characters used to represent a reserved character in HTML. There are three types, named character references: `&lt;`; decimal numeric reference: `&#169;`; hexadecimal numeric  reference `&#x20AC;`;

- {{ddmenu('Separation of concerns')}} is a design principle where you separate your programs into distinct sections and have each section address a separate concern.

- There are three tools to consider when using media, such as images, on your web pages: the {{ddmenu_u('size', 'format', 'compression')}}#.

- It's worth noting that specific file formats, such as JPG, are not lossless.  Lossless means that the original data can be perfectly reconstructed from the compressed data

- By default, images are released as all rights reserved. 

- Common image formats like PNG and JPG are classified as raster formats. This essentially means that they are pixel-based, with the data tracking the color value in each pixel.

- SVG stands for a scalable vector graphic. A vector graphic tracks data based on paths and equations to plot points, lines, and curves. 
SVGs specifically have the added benefit of storing data in XML.

- `referrerpolicy` attribute and set it to `strict-origin-when-cross-origin`. This shares the full address on the same site, only the site name on other sites, and nothing on insecure sites. which displaied in the `Request Header`.

- There are five different states a link can be in. `:link, :visited, :hover, :focus, :active`

- The term `href` stands for Hypertext Reference.

- In HTML, the `#` (hash) symbol refers to a fragment identifier. When used alone in an `href` attribute, it acts as a placeholder or a "top of page" link.

- There are two common forms of abbreviations: acronyms and initialisms. The distinction is acronyms are pronounced as words and initialisms are pronounced as individual letters.

- A superscript `sup` is a symbol or letter printed above the normal line of text. It is important to note that the superscript element should only be used for typographical reasons. 

-  Default styling of content inside of the code element is a monospaced font

- in HTML5, the u element should only be used to indicate that text has non-textual annotation applied.

- The strikethrough element, or `s` element for short, should be used to represent when text is no longer accurate or relevant.

- Lorem ipsum is commonly used in web development to serve as placeholder text. 


# Boilerplate
- Version 1

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta
       name="viewport"
       content="width=device-width, initial-scale=1.0" />
    <title>freeCodeCamp</title>
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
  </body>
</html>
```
