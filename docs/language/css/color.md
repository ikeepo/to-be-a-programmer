# Color
## Color Theory in Design
Color theory is the study of how colors interact with each other and how they affect our perception
## Concepts
- A {{ddmenu('color scheme')}} is the set of colors chosen for a specific design or project. 

    - Analogous color schemes

    - Complementary color schemes 

    - triadic color scheme 
    
    - monochromatic color scheme

- {{ddmenu('Named colors')}} are predefined color names recognized by browsers. Named colors in CSS are a collection of {{ddmenu('140')}} [standard color names](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color) like red, blue, yellow, aqua, fuchsia, black, and so on.

- the primary colors of light: RGB(自发光，additive color model); the primary colors of paint: RYB（反射光，减色）;

- 编程主要是加色(`rgb(0,0,0), rgba(0-255,0-255,0-255,0-1`)，因为代码都是通过屏幕发光呈现的。平板是加色，kindle是减色。

- HSL stands for Hue[0-360], Saturation[0-100%], and Lightness[0-100%]
    
    - The hue is the color type

    - Saturation refers to the intensity or purity of the color.

    - Lightness determines how light or dark the color is

- `hsl(hue saturation lightness), hsl(hue saturation lightness / alpha), hsla(hue, saturation, lightness, alpha)`, 数学上的关系是：$H \times S \times L$ 的连续组合，完整映射了 $R \times G \times B$ 的全部空间。

- A hex code (short for hexadecimal code) is a six-character string used to represent colors in the RGB color model. The first two characters represent the red value, the next two represent green, and the last two represent blue.

- hex 16进制和rgb的255有什么对应关系？`F * 16 + F = 240 + 15 = 255`

-  `#FFFFFF` (white) can be written as `#FFF`.

- Gradients in CSS allow you to create smooth transitions between two or more specified colors. 

- Linear gradients(`linear-gradient(to right/45deg, red 20%, blue, ...);`) create a gradual blend between colors along a straight line. linear-gradient function actually creates an image element

- Radial gradients(`radial-gradient(circle/ellipse at top left, red, blue)`), on the other hand, create circular or elliptical gradients that radiate from a central point.

-   background: linear-gradient(to right, red 20%, yellow 40%, blue 80%); 为什么数值加起来不是100？ it means the color stops at precise positions. 0-20%是纯红，20-40%是红变黄，40%位置纯黄，40-80%是黄变蓝，80%及以后是纯蓝。
