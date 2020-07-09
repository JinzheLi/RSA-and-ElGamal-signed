#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 14:33
# @Author  : 李金哲
# @Site    : 
# @File    : tip.py
# @Software: PyCharm

import wx
import wx.xrc
"""
质数长度提示窗口
"""
class tip(wx.Frame):
    def __init__(self, parent, lenth):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"提示窗口", pos=wx.DefaultPosition, size=wx.Size(304, 214),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetBackgroundColour('#f0d05b')

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        self.lenth = lenth
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"质数长度推荐在20位以内，若大于20位，可能花费很长的运行时间", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer3.Add(self.m_staticText5, 1, wx.ALL, 5)

        gSizer17 = wx.GridSizer(0, 2, 0, 0)

        self.button1 = wx.Button(self, wx.ID_ANY, u"继续", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer17.Add(self.button1, 0, wx.ALL, 5)

        self.button2 = wx.Button(self, wx.ID_ANY, u"返回", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer17.Add(self.button2, 0, wx.ALL, 5)

        bSizer3.Add(gSizer17, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.button1.Bind(wx.EVT_BUTTON, self.go_to)
        self.button2.Bind(wx.EVT_BUTTON, self.channel)

    def __del__(self):
        self.Destroy()

    # Virtual event handlers, overide them in your derived class
    def go_to(self, event):
        self.__del__()
        from Gui.ElGamal.key_result import MyDialog5
        myframe = MyDialog5(None,self.lenth)
        myframe.Show(True)

    def channel(self, event):
        self.Destroy()

