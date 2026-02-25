# Anchor - Chinese
## Abstract
默认不支持中文，只识别标题中的英文部分，比如 `动词变位：er类`就只识别为`#er` anchor.

配置如下后可以识别中文

## Config
```mkdocs.yml
markdown_extensions:
  - toc:
      permalink: true  # (可选) 会在标题旁显示一个链接符号，方便调试
      slugify: !!python/name:pymdownx.slugs.uslugify # 强烈建议：支持中文锚点
  - attr_list # 允许你手动定义 ID
```
