#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 16:52
# @Author  : 李金哲
# @Site    :
# @File    : enter.py
# @Software: PyCharm

# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame2
###########################################################################
"""
程序总入口
"""
class MyFrame2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u'数字签名系统', pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour('#f0d05b')

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"欢迎使用数字签名系统！", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(wx.Font(22, 70, 90, 90, False, "宋体"))

        bSizer4.Add(self.m_staticText3, 0, wx.ALL, 5)

        bSizer3.Add(bSizer4, 1, wx.EXPAND, 5)

        gSizer2 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"RSA数字签名系统", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        self.m_staticText4.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

        gSizer2.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"ElGamal数字签名系统", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        self.m_staticText5.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

        gSizer2.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"RSA", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_button2, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"ElGamal", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_button3, 0, wx.ALL, 5)

        bSizer3.Add(gSizer2, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button2.Bind(wx.EVT_BUTTON, self.rsa_enter)
        self.m_button3.Bind(wx.EVT_BUTTON, self.elgamal_enter)

    def __del__(self):
        self.Destroy()

    # Virtual event handlers, overide them in your derived class
    def rsa_enter(self, event):
        from Gui.RSA.Main import RSA_main
        myframe = RSA_main(None)
        myframe.Show(True)
        self.__del__()


    def elgamal_enter(self, event):
        from Gui.ElGamal.Main import Elgamal
        myframe = Elgamal(None)
        myframe.Show(True)
        self.__del__()
