# [mkdocs](https://www.mkdocs.org/user-guide/writing-your-docs/)
## How to add a comment module in mkdocs 
[giscus](https://github.com/giscus/giscus)

```shell
1. Repo --> Settings --> General --> Features --> Discussion(active)
2. Install Github App giscus --> access to the target repo;
3. https://giscus.app/ --> github_id/repo_name --> Discussion 的标题包含页面的 pathname --> announcements -->  data-repo-id & data-category-id From the Script 
4. mkdocs.yml 
theme:
  name: material
  custom_dir: overrides
extra:
  comments:
    provider: giscus
    options:
      repo: 你的用户名/仓库名
      repo_id: MDEwOlJlcG9zaXRvcnkz... # 替换为你获取的值
      category: Announcements
      category_id: DIC_kwDOEn... # 替换为你获取的值
      mapping: pathname
      strict: 0
      reactions_enabled: 1
      emit_metadata: 0
      input_position: bottom
      theme: preferred_color_scheme # 自动跟随主题深色/浅色
      lang: zh-CN
5. root dir overrides/main.html
```

- How to forbid comments
```shell
---
comments: false
---
```
## markdown-extensions
### pymdownx.tasklist

```shell
- markdown_extensions:
  - pymdownx.tasklist:
      custom_checkbox: true  # Optional: Makes checkboxes look better
      clickable_checkbox: true # Allows users to toggle them (UI only)
```

- How to add checkbox in mkdocs
`- [x]`

## Plugins

- [ mkdocs ](https://mkdocs-macros-plugin.readthedocs.io/en/latest/)-macros-plugin  

自定义宏；mkdocs层面的自动化功能；   

step1 : `pip install mkdocs-macros-plugin`  

step2: `在mkdocs.yml中plugins下添加macros`  

step3: `在main.py中define_env下添加函数`
```
def define_env(env):
    @env.macro
    def ddmenu(answer, *options):
        html = f'<select onchange="this.style.backgroundColor = (this.value == \'{answer}\' ? \'transparent\' : \'#ffcccc\');" style="border: none; border-bottom: 2px solid gray; font-weight: bold; padding: 2px; cursor: pointer;">'
        html += '<option value="">???</option>'
        # 把正确答案也放进选项
        all_opts = [answer] + list(options)
        for opt in all_opts:
            html += f'<option value="{opt}">{opt}</option>'
        html += '</select>'
        return html
```

step4: `在md中调用 There are {*2 ddmenu('six', 'five', 'seven') }*2 heading elements.`

- [git-revision-date-localized](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin)
display the date of the last git modification of a page.


## How to publish the site to local LAN 
```shell 
ifconfig 
# en0找到本地局域网ip,inet 后面192开头的
# en0 表示以太网接口0，通常是wifi，如果连接了网线还会有en1 等
mkdocs serve -a 0.0.0.0:8000 
# 局域网内通过192...:8000访问
```
## icons in mkdocs
This is the domain of [material for mkdocs](https://squidfunk.github.io/mkdocs-material/getting-started/).
How to use [Icons, Emojis](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/#with-colors-docsstylesheetsextracss) can be found here. On the head of the page, there is a [`Search`](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/#search) input which is used to find the exact code for icons/emojis you need like `:smile:`, but you should set the [setting](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/#configuration) first
# Errors
1. `could not determine a constructor for the tag 'tag:yaml.org,2002:python/name:material.extensions.emoji.twemoji'
  in "mkdocs.yml", line 14, column 20` happened in pre-commit
Same problem can be found in pre-commit issues [552](https://github.com/pre-commit/pre-commit-hooks/issues/552)
```
# in the .pre-commit-config.yaml
args: [--unsafe]
```
# Authntication
> [Access private MkDocs after logging in #5875](https://github.com/squidfunk/mkdocs-material/discussions/5875)  [OAuth2 Proxy](https://github.com/meadapt/login-static-site)(Active)
