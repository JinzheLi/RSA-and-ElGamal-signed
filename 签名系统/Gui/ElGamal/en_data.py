# -*- coding: utf-8 -*-
"""
加密界面
"""
###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyDialog2
###########################################################################

class MyDialog2(wx.Frame):

    def __init__(self, parent, data = None, path = None):
        self.data = data
        self.path = path
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(558, 491), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetBackgroundColour('#f0d05b')

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.title = wx.StaticText(self, wx.ID_ANY, u"签名界面", wx.DefaultPosition, wx.DefaultSize, 0)
        self.title.Wrap(-1)
        self.title.SetFont(wx.Font(24, 70, 90, 90, False, "宋体"))
        bSizer2.Add(self.title, 0, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"公开参数 p", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))
        gSizer1.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.p_data = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(240, -1), 0)
        gSizer1.Add(self.p_data, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(gSizer1, 1, wx.EXPAND, 5)

        gSizer2 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"公开参数 g", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))
        gSizer2.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.g_data = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(240, -1), 0)
        gSizer2.Add(self.g_data, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(gSizer2, 1, wx.EXPAND, 5)

        gSizer21 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText31 = wx.StaticText(self, wx.ID_ANY, u"公开参数 y", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        self.m_staticText31.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))
        gSizer21.Add(self.m_staticText31, 1, wx.ALL | wx.EXPAND, 5)

        self.y_data = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(240, -1), 0)
        gSizer21.Add(self.y_data, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(gSizer21, 1, wx.EXPAND, 5)

        gSizer7 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"签名文件保存路径（文件名默认为 c1.txt 和 c2.txt ）", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        self.m_staticText7.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))
        gSizer7.Add(self.m_staticText7, 1, wx.ALL | wx.EXPAND, 5)

        self.m_dirPicker2 = wx.DirPickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition,
                                             wx.Size(250, -1), wx.DIRP_DEFAULT_STYLE)
        gSizer7.Add(self.m_dirPicker2, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(gSizer7, 1, wx.EXPAND, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"签名", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button1, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button1.Bind(wx.EVT_BUTTON, self.do_on)

    def __del__(self):
        self.Destroy()

    # Virtual event handlers, overide them in your derived class
    def do_on(self, event):
        p = int(self.p_data.GetValue())
        g = int(self.g_data.GetValue())
        y = int(self.y_data.GetValue())

        from model import ElGamal
        if self.path is not None:
            if p and g and y and self.m_dirPicker2.GetPath():
                path1, path2, len1, len2 = ElGamal.data_encrypt(p, g, y, path=self.path, c_path=self.m_dirPicker2.GetPath())
            self.__del__()

        if self.data is not None:
            if p and g and y and self.m_dirPicker2.GetPath():
                path1, path2, len1, len2 = ElGamal.data_encrypt(p, g, y, m_data=self.data, c_path=self.m_dirPicker2.GetPath())
            self.__del__()

        from Gui.ElGamal.en_result import x_result
        myframe = x_result(None, path_1=path1, path_2=path2, len_1=str(len1), len_2=str(len2))
        myframe.Show(True)
