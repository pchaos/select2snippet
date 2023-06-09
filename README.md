# select2snippet

* Created: 2023-06-08 18:14:39
* Last Modified: 2023-06-09 16:55:05

This is a Neovim plugin that provides selected text convert to snnippet, paste to clipboard.

```
.
├── plugin
│   └── select2snippet.py
├── rplugin
│   └── python3
│       └── select2snippet.py
├── templates
│   ├── default.j2
│   ├── html.j2
│   └── python.j2
└── README.md
```

* plugin 目录存放普通的 Vim 插件脚本，包括 Python 和 VimL 脚本。
* rplugin/python3 目录存放 NeoVim 插件脚本，使用 Python 3 编写。
* templates 目录存放 Jinja2 模板，这里包括了一个名为 html.j2 的 HTML 模板和一个名为 python.j2 的 Python 模板，你可以根据需要添加更多的模板。
* README.md 文件是插件的说明文档，你可以在其中提供插件用法和注意事项。
