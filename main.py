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
