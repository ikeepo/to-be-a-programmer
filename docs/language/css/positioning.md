# Positioning
# Concepts
- Floats in CSS are a technique originally designed to allow text to wrap around an element, such as an image.

- positioning allows us to control how elements are laid out on a page.

    - static positioning(default) 
    
    - relative positioning

- {{ddmenu('Absolute positioning')}} allows you to take an element out of the normal document flow, making it behave independently from other elements. 

- CSS positioning strategies:
    
    - `position: absolute`: removes an element from the document flow and positions it relative to the nearest positioned ancestor(any parent element that has position: `relative`, `absolute`, or `fixed`), or the initial containing block if none exists. 

    - `position: fixed`: it is removed from the normal document flow and placed relative to the viewport,

    - `position: sticky`: behaves as a hybrid between relative and fixed positioning. 

- The {{ddmenu('z-index')}} property in CSS is used to control the vertical stacking order of positioned elements that overlap on the page.

- the {{ddmenu('z-index')}} only works on elements that are positioned

- 
