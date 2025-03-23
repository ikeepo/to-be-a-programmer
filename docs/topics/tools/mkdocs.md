# [mkdocs](https://www.mkdocs.org/user-guide/writing-your-docs/)

## icons in mkdocs
This is the domain of [material for mkdocs](https://squidfunk.github.io/mkdocs-material/getting-started/).
How to use [Icons, Emojis](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/#with-colors-docsstylesheetsextracss) can be found here. On the head of the page, there is a [`Search`](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/#search) input which is used to find the exact code for icons/emojis you need like `:smile:`
# Errors
1. `could not determine a constructor for the tag 'tag:yaml.org,2002:python/name:material.extensions.emoji.twemoji'
  in "mkdocs.yml", line 14, column 20` happened in pre-commit
Same problem can be found in pre-commit issues [552](https://github.com/pre-commit/pre-commit-hooks/issues/552)
```
# in the .pre-commit-config.yaml
args: [--unsafe]
```
