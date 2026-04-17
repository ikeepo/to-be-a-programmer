# [mkdocs-timetoread-plugin](https://pypi.org/project/mkdocs-timetoread-plugin/)
# 如何显示字数

## 在html中设置反推

## 在overrides/main.html中增加
```shell
{# 1. 在内容渲染前插入统计信息 #}
  {% if not page.is_homepage %}
    <div style="margin-bottom: 1rem; opacity: 0.8; font-size: 0.8em;">
      {# 尝试调用插件可能暴露的字数变量 #}
      {% if page.stats and page.stats.words %}
        <span>📝 字数：{{ page.stats.words }} 字</span>
      {% elif page.word_count %}
        <span>📝 字数：{{ page.word_count }} 字</span>
      {% endif %}

      {# 显示已正常工作的阅读时间 #}
      {% if page.reading_time %}
        <span style="margin-left: 10px;">⏳ 阅读时间：{{ page.reading_time }} 分钟</span>
      {% endif %}
    </div>
  {% endif %}
```


