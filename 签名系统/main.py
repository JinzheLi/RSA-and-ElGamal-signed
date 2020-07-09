#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 14:31
# @Author  : 李金哲
# @Site    :
# @File    : main.py
# @Software: PyCharm
from Gui.enter import MyFrame2
import wx
if __name__ == '__main__':
    app = wx.App(False)

    SiteFrame = MyFrame2(None)
    SiteFrame.Show()

    app.MainLoop()
