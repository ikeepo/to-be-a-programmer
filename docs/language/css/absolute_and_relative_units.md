# Absolute and Relative Units 
## Absolute Units 
`Absolute length units are of fixed length and are not relative to anything else. `

```shell
- px = It is important to note that while 1px is standardized as 1/96th of an inch for the purposes of CSS layout, the actual physical size of a pixel may differ depending on the display.

- in (inches) unit, which is equal to 96px
- cm (centimeters) unit, which is equal to 25.2/64 of an inch
- mm (millimeters) unit, which is equal to 1/10th of a centimeter
- q (quarter-millimeters) unit, which is equal to 1/40th of a centimeter
- pc (picas) unit, which is equal to 1/6th of an inch
- pt (points) unit, which is equal to 1/72th of an inch
```

### 既然是1/96 inch,为什么可能不同? 

因为浏览器会根据DPR(Device Pixel Ratio，由浏览器实现，根据硬件+操作系统共同决定)调整；

## Relative Units 
### Percentages 
`in CSS are relative units that allow you to define sizes, dimensions, and other properties as a proportion of their parent element. `

### `em` & `rem`
`em` units are relative to the font size of the element. If you are using ems for the font-size property, the size of the text will be relative to the font size of the parent element.

A `rem` unit is relative to the font size of the root element, which is the `html` element.
### `vh` & `vw`
`vh and vw are viewport-relative units that allow you to size elements based on the dimensions of the browser window. These units are particularly useful for creating responsive designs that adapt to different screen sizes.`

 `1vh` is equal to 1% of the viewport's height.
### `calc()`
You can perform calculations on values that represent length, angle, time, percentages, numbers, and colors. You can also combine different units like pixels, percentages, and ems.

With numbers, all the values in the expression, also called the operands, must have their corresponding units, like px, em, and percentage (%). Depending on the operator, different operands may have different units.
