# Responsive Design
# Concepts
- Responsive web design is an approach to web development that aims to create websites that provide an optimal viewing and interaction experience across a wide range of devices

- The core principle of responsive design is {{ddmenu('adaptability')}}: the ability of a website to adjust its layout and content based on the screen size and capabilities of the device it's being viewed on.

- Responsive design typically relies on three main components:

  - {{ddmenu('Fluid grids')}} use relative units like percentages instead of fixed units like pixels, allowing content to resize and reflow based on screen size.

  - {{ddmenu('Flexible images')}} are set to resize within their containing elements, ensuring they don't overflow their containers on smaller screens.

  - {{ddmenu('Media queries')}} allow developers to apply different styles based on the characteristics of the device, primarily the viewport width.

- {{ddmenu('CSS Grid')}} and {{ddmenu('Flexbox')}} are practical tools that make implementing responsive designs much easier and more efficient.

- {{ddmenu('Flexbox')}} is typically used for components and one-dimensional layouts, while {{ddmenu('Grid')}} is used for overall page structure and two-dimensional layouts.

- media queries:

```shell
@media mediatype and (feature: value) and/,/not/only ... {
  /* CSS rules go here */
}
```

- what the query mean in "media queries"? While media queries use a **conditional / query-based model** ("ask first, then apply"), regular CSS uses a **declarative rule-matching model**.

- `mediatype`: `all, print, screen`

- `feature`
  
    - `min/max - height/width`

    - `aspect-ratio`

    - `orientation`: `landscape | portrait`

    - `resolution`

    - `hover`

    - `prefers-color-scheme`

- Why does CSS use the terms 'landscape' and 'portrait' instead of 'horizontal' and 'vertical'?CSS uses portrait and landscape because they refer to the aspect ratio of a 2D surface, whereas "horizontal" and "vertical" refer to 1D directions or axes.

- A common pattern ("mobile-first" responsive design) is to define a base style for mobile devices and then use media queries to enhance the layout for larger screens

- {{ddmenu('Media breakpoints')}} are specific points in a website's design where the layout and content adjust to accommodate different screen sizes. 
    
    - `480px`

    - `576px / 640px`
    
    - `768px`
    
    - `992px`
    
    - `1200px / 1024px`
    
    - `1400px`

- Google uses mobile-first indexing, meaning it predominantly uses the mobile version of the content for indexing and ranking.
