# https://mkdocs-macros-plugin.readthedocs.io/en/latest/
# This is for mkdocs macros
def define_env(env):
    """
    This is the hook for the variables, macros and filters.
    """

    @env.macro
    def price(unit_price, no):
        "Calculate price"
        return unit_price * no

    # 添加下拉框
    @env.macro
    def ddmenu(answer, *options):
        html = f"<select onchange=\"this.style.backgroundColor = (this.value == '{answer}' ? 'transparent' : '#ffcccc');\" style=\"border: none; border-bottom: 2px solid gray; font-weight: bold; padding: 2px; cursor: pointer;\">"
        html += '<option value="">???</option>'
        # 把正确答案也放进选项
        all_opts = [answer] + list(options)
        for opt in all_opts:
            html += f'<option value="{opt}">{opt}</option>'
        html += "</select>"
        return html

    # 添加下拉框, 所有都对，背景无区别
    @env.macro
    def ddmenu_u(answer, *options):
        html = f'<select style="border: none; border-bottom: 2px solid gray; font-weight: bold; padding: 2px; cursor: pointer;">'
        html += '<option value="">???</option>'
        # 把正确答案也放进选项
        all_opts = [answer] + list(options)
        for opt in all_opts:
            html += f'<option value="{opt}">{opt}</option>'
        html += "</select>"
        return html

    # 添加法语发音宏
    @env.macro
    def fr(text):
        """
        生成一个点击可发音的法语单词链接
        用法: {{ fr('Bonjour') }}
        """
        # 这里调用我们之前在 tts.js 里定义的 speakFrench 函数
        return f'<span class="fr-word" onclick="speakFrench(\'{text}\')">{text}</span>'

    # 添加中文发音宏
    @env.macro
    def zh(text):
        """
        生成一个点击可发音的中文单词链接
        用法: {{ zh('你好') }}
        """
        # 调用 tts.js 里定义的 speakChinese 函数
        return f'<span class="zh-word" onclick="speakChinese(\'{text}\')">{text}</span>'

    # 生成时间线
    @env.macro
    def generate_timeline():
        """
        自动遍历所有文章，生成带有 data-date 属性的 HTML 列表，供前端 JS 进行动态筛选。
        """
        docs_dir = env.config["docs_dir"]
        all_posts = []

        # 1. 遍历 docs 目录下的所有文件
        for root, dirs, files in os.walk(docs_dir):
            for file in files:
                # 排除非 Markdown 文件以及 timeline.md 自身（避免无限循环或把自己列进去）
                if file.endswith(".md") and file != "timeline.md":
                    file_path = os.path.join(root, file)

                    # 获取文件的最后修改时间
                    # 注意：os.path.getmtime 在本地开发时很准。
                    # 如果在 CI/CD 环境部署，请确保配置了 git fetch-depth: 0 以便 Git 插件正确注入时间戳
                    mtime = datetime.fromtimestamp(os.path.getmtime(file_path))

                    # 计算相对路径用于生成正确的网站 URL 链接
                    rel_path = os.path.relpath(file_path, docs_dir).replace("\\", "/")
                    web_path = rel_path.replace(".md", "/")

                    # 处理首页 index.md 的特殊链接规范
                    if web_path.endswith("index/"):
                        web_path = web_path[:-6]

                    # 尝试读取 Markdown 的第一行 `# 标题` 作为文章名，读取不到则使用文件名
                    title = file[:-3]
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            for line in f:
                                line = line.strip()
                                if line.startswith("# "):
                                    title = line[2:]
                                    break
                                # 兼容支持从 Front-matter (YAML) 中读取 title
                                elif line.startswith("title:"):
                                    title = (
                                        line.split(":", 1)[1]
                                        .strip()
                                        .strip('"')
                                        .strip("'")
                                    )
                                    break
                    except Exception:
                        pass

                    # 记录文章信息
                    all_posts.append(
                        {
                            "title": title,
                            "path": f"{env.config['site_url'] or '/'}{web_path}",
                            "date_str": mtime.strftime(
                                "%Y-%m-%d"
                            ),  # 用于前端显示的日期
                            "date_obj": mtime,  # 用于后端排序的日期对象
                        }
                    )

        # 2. 按最后修改时间倒序排列（最新的在最上面）
        all_posts.sort(key=lambda x: x["date_obj"], reverse=True)

        # 3. 构造 HTML 字符串
        if not all_posts:
            return "<p>暂无文章</p>"

        html = '<ul id="timeline-list" style="list-style: none; padding-left: 0;">\n'
        for post in all_posts:
            html += f'  <li class="timeline-item" data-date="{post["date_str"]}" style="margin-bottom: 12px; display: block;">\n'
            html += f'    <span class="post-date" style="font-family: monospace; color: #6e7781; margin-right: 15px;">[{post["date_str"]}]</span>\n'
            html += f'    <a class="post-link" href="{post["path"]}" style="font-weight: 500;">{post["title"]}</a>\n'
            html += f"  </li>\n"
        html += "</ul>\n"

        return html
