# CSS Best Practice
# Color
## What are the current best practices for building a CSS color system?

- [Evil Martians: OKLCH in CSS](https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl)

- [oklch](https://oklch.com/#0.7,0.1,339,100)

- [Design System Repo](https://designsystemsrepo.com): Ref

## Ready to use color themes
- [Realtime Colors](https://www.realtimecolors.com/?colors=050316-fbfbfe-2f27ce-dddbff-443dff&fonts=Inter-Inter)
- [Coolors](https://coolors.co)

- [Radix](https://www.radix-ui.com/colors)

- [Happy Hues](https://www.happyhues.co)

# Is it necessary to master css compiler to master CSS
CSS 预编译器（如Sass、Less、PostCSS）本质上只是字符串处理与语法糖转换工具，把嵌套语法、变量、函数转换成标准的原生 CSS。

使用css并不需要懂CSS是如何编译的，但是需要搞懂**浏览器拿到CSS后做了什么**
.
So, what's the metal model for css experts:

- CSS for JavaScript Developers, Josh W. Comeau, online course

- Heydon Pickering 

  - [Inclusive Components](<./books/Inclusive Components.epub>) 

  - [Every Layout](<./books/Every Layout.pdf>)
    
      - 不要试图去‘控制’元素的绝对位置和大小，而是给元素一套‘生长规则’，让浏览器自己去计算布局。

      - 把浏览器页面布局抽象成几种类型，每一个章节描述一种布局类型，这种布局类型在定义的时候，不是从下往上一个一个细节定义好，而是从上往下、从大往小定义组件的边界(Layout Boundaries)及变化规则，当填充内容(Intrinsic Content)的时候，内容会充满组件就像气球被充气从而让布局自然生成o

      - imperative thinking ==> Declarative/Defensive Thinking

- Rachel Andrew

  - The New CSS Layout
    
      - CSS 是一组切换浏览器渲染算法的开关

- Jen Simmons
    
    - [Layout Land](https://www.youtube.com/@LayoutLand/videos)

    - Intrinsic Web Design

# 不管是哪个角度，想要深度掌握CSS，都需要了解浏览器对CSS的渲染逻辑链条Rendering Pipeline
"CSS: The Definitive Guide" 主要讲规则(W3C domain)，Rendering Pipeline跨越W3C、浏览器底层工程、计算机图形学（GPU），尚无专著专门论述这个角度。


- [How Browsers Work: Behind the scenes of modern web browsers](https://webplatform.github.io/docs/concepts/Internet_and_Web/how_browsers_work/) - Tali Garsiel,

- High Performance JavaScript - Nicholas C. Zakas, Chapter 6

- High Performance Browser Networking - Ilya Grigorik, Critical Rendering Path


- Rendering Performance - Google Chrome web.dev, Pixel Pipeline

