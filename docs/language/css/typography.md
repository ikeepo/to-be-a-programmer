# Typography
# Concepts
- {{ddmenu('Typography')}} is the art of choosing the right fonts and format to make text visually appealing and easy to read. 

- Fundamental elements of **typography**:
    
    - baseline

    - cap height

    - x-height

    - ascenders 

    - descenders 

    - kerning

    - tracking

    - leading

- Other factors that enhance the readability of your content and reinforce your brand's identity: 
    
    - line length

    - underling

    - italic 

    - fonts 

    - spacing

    - hierarchy

- A {{ddmenu('typeface')}} is the overall design and style of a set of characters, numbers, and symbols. It's like a blueprint for a family(weight, style, width) of {{ddmenu('fonts')}}. 

- A {{ddmenu('font')}} is a specific variation of a typeface with specific characteristics, such as size, weight, style, and width.

- Web Content Accessibility Guidelines

- A {{ddmenu('font family')}} is a group of fonts that share a common design. 

- `font-family: Arial, Lato;`： The selection process doesn't stop if the first font is available. The font family is chosen one character at a time, so if a font lacks a specific character, the browser looks for it in the lower-priority fonts. 

- generic font family :

  - serif

  - sans-serif

  - monospace
  
  - cursive

  - fantasy

-  {{ddmenu('Web-safe fonts')}} are a subset of fonts that are very likely to be installed on a computer or device.

- Web-safe fonts vs generic font family ==> font vs typeface

- {{ddmenu('At-rules')}} are statements that provide instructions to the browser.

- With `@font-face`, you can define a custom font by specifying the font file, format, and other important properties, like weight and style. 

```shell
@font-face {
  font-family: "MyCustomFont"; 
  src: url("path/to/font.woff2") format("woff2"),
    url("path/to/font.otf") format("opentype")  tech(color-COLRv1),
    url("path/to/font.woff") format("woff");
}
```

- Possible font formats include `collection, embedded-opentype, opentype, svg, truetype, woff, and woff2`.

- External Fonts:

    - [Google Fonts](https://fonts.google.com)

    - [Font Squirrel](https://www.fontsquirrel.com)

- `text-shadow`: offset, blur, and color


