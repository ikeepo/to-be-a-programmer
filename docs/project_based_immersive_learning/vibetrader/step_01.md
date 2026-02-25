# First Step
## Read Readme.md
运行
## Questions
### why use `tsc -b` before build
Vite只strip类型标注，turn ts --> js, 不管对错，只转换。

`tsc` works as type police for accuracy.
### tsc的功能是将ts转成js
`-b` means build mode, it's for incremental compilation. 
生成的文件位置取决于`tsconfig.json`中的配置，
### 如何理解这个tsconfig.json
```shell 
{
    "files": [],  # 不要在这个根目录下寻找代码文件，去references找
    "references": [
        {
            "path": "./tsconfig.app.json" # 浏览器端代码
        },
        {
            "path": "./tsconfig.node.json" # node.js 环境代码
        }
    ]
}
```

### 如何配置`tsc`只检查不生成`js`
`tsconfig.app/node.json`中`noEmit: true`表示只检查ts格式，不生成js;相反如果是false且配置`outDir`，就会生成js。

这是`vite`引导程序自动配置的，也就是说，是`vite`默认采用`tsc -b && vite build`这个逻辑。

### `src/App.tsx` vs `src/main.tsx`
`main.tsx`是项目入口，`App.tsx`是前端React的入口。

分开是为了保持文件指责的单一。

这些也是`vite`默认配置。
