#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TIKTOK AI智能翻译助手
主要功能：
1. 语音实时翻译
2. 屏幕文字识别与翻译
3. 多国语言支持
4. 翻译结果保存
"""

import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
from ui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    
    # 设置应用程序信息
    app.setApplicationName("TIKTOK AI智能翻译助手")
    app.setApplicationVersion("1.0.0")
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()