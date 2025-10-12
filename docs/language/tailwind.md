# Tailwind

# Why Tailwind need `tailwind.config.js` `postcss.config.mjs` such two config file
The first is for tailwind itself, tailwind uses postcss internally.
Postcss is a tool for transforming CSS with JS plugins.
# Tailwind uses a **rem-based spacing system**
1 = 0.25rem = 4px    
1rem = 16px  
`rem` means `root em`, relative to the root element's font size which is defined in the `<html>` element as `font-size: 16px`;
## arbitrary values
`lg:h-[60px]`
