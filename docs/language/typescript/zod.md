# Zod 
## Question 
### `Attempted import error: 'ZodEffects' is not exported from 'zod' (imported as 'ZodEffects').`
zod新版本去除`z.ZodEffects`, 但是@conform-to/zod还在使用，后者升版本无效，只能前者降版本。
```shell 
npm install zod@3.22.4
```
