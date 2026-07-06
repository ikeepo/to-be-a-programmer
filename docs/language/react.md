# React
## Questions
### React vs React-Native
React 是 UI 的抽象建模语言（跨 Web / Native 的“领域层”），React Native 是把这个模型（component + state + props）映射到移动操作系统原生组件上的执行层。

React： 用 React 模型 → 生成 Web UI（DOM）

React Native：用 React 模型 → 生成 iOS / Android 原生 UI
### R, RN, Expo
```shell
React (2013)
   ↓ UI抽象层; 把 UI 变成函数; 解决 Web UI 的复杂性
React Native (2015)
   ↓ 跨平台 UI runtime; 把 UI 函数搬到手机; 解决 iOS + Android 重复开发问题
Expo (2016+)
   ↓ 开发/构建/运行平台; 把“搬运过程”自动化 + 产品化; 解决 React Native “太难用、太工程化”的问题
```

Expo 编译成 Web 时，是把 React Native 代码通过 react-native-web 转译成 React DOM 能渲染的组件。
