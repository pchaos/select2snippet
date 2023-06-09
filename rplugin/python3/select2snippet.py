# -*- coding: utf-8 -*-

import sys

sys.path.append("/home/user/.local/lib/python3.10/site-packages")

import clipboard
import pynvim
from jinja2 import Environment, FileSystemLoader

# Last Modified: 2023-06-09 12:44:28


@pynvim.plugin
class Select_2_Snippet:
    def __init__(self, nvim):
        self.nvim = nvim
        self.default_template = "default.j2"
        loader = FileSystemLoader("templates/")
        self.env = Environment(loader=loader)

    @pynvim.command("switch_template", nargs=1)
    def switch_template(self, template_name="default.j2"):
        if not self.env.get_template(template_name):
            raise ValueError("Unknown template")
        self.default_template = template_name

    def render_template(self, **kwargs):
        template = self.env.get_template(self.default_template)
        return template.render(**kwargs)

    @pynvim.command("Select2Snippet", nargs="*", range="")
    def add_template(self, args, range):
        # 获取当前模式下的文本
        text = None
        # mode = self.nvim.funcs.mode()
        current_mode = self.nvim.eval("mode()")
        if current_mode == "v":
            # 获取当前用户选择的区域（如果有选择的话）
            start, end = self.nvim.current.range
            if start == end:
                # 如果没有选择区域，则获取当前光标所在的位置
                pos = self.nvim.current.window.cursor
            else:
                # selected text
                text = "\n".join(self.nvim.current.buffer[i] for i in range(*range))
        if not text:
            try:
                if args[0] == "word":
                    # select word
                    text = self.nvim.eval('expand("<cword>")')
                else:
                    # select line
                    text = self.nvim.current.line
            except TypeError:
                pass

        # 渲染模板并将结果复制到系统剪切板中
        snippet = self.render_template(text=text)

        clipboard.copy(snippet)

        print(f"vim mode:{current_mode}. Copied to clipboard: {snippet}")


if __name__ == "__main__":
    import pynvim

    nvim = pynvim.attach("child")
    Select_2_Snippet(nvim).start()
