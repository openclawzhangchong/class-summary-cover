# -*- coding: utf-8 -*-
"""班级实习材料汇总封面 - 桌面打印工具"""
import sys
import os
import webview


def resource_path(rel):
    """兼容 PyInstaller 打包后的资源路径"""
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, rel)


def main():
    html_path = resource_path("summary_cover.html")
    webview.create_window(
        "班级实习材料汇总封面",
        html_path,
        width=920,
        height=1080,
        min_size=(800, 600),
    )
    webview.start()


if __name__ == "__main__":
    main()
