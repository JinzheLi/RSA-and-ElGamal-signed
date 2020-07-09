# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

"""
解密参数界面
"""

###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3(wx.Frame):

    def __init__(self, parent, c1_path, c2_path, file=True):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(493, 498), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetBackgroundColour('#f0d05b')

        self.file  = file
        self.c1_path = c1_path
        self.c2_path = c2_path

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, u"验证操作", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        self.m_staticText12.SetFont(wx.Font(24, 70, 90, 90, False, "宋体"))
        bSizer7.Add(self.m_staticText12, 0, wx.ALL | wx.EXPAND, 5)

        bSizer6.Add(bSizer7, 1, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        gSizer14 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText13 = wx.StaticText(self, wx.ID_ANY, u"签名文档 c1 规范长度", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)
        self.m_staticText13.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))
        gSizer14.Add(self.m_staticText13, 0, wx.ALL, 5)

        self.m_staticText14 = wx.StaticText(self, wx.ID_ANY, u"签名文档 c2 规范长度", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)
        self.m_staticText14.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))
        gSizer14.Add(self.m_staticText14, 0, wx.ALL, 5)

        self.c1_len = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        gSizer14.Add(self.c1_len, 0, wx.ALL, 5)

        self.c2_len = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        gSizer14.Add(self.c2_len, 0, wx.ALL, 5)

        bSizer10.Add(gSizer14, 1, wx.EXPAND, 5)

        bSizer6.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        gSizer16 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText19 = wx.StaticText(self, wx.ID_ANY, u"公开参数 p", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText19.Wrap(-1)
        self.m_staticText19.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))
        gSizer16.Add(self.m_staticText19, 0, wx.ALL, 5)

        self.m_staticText20 = wx.StaticText(self, wx.ID_ANY, u"私人秘钥 x", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText20.Wrap(-1)
        self.m_staticText20.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))
        gSizer16.Add(self.m_staticText20, 0, wx.ALL, 5)

        self.m_textCtrl15 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        gSizer16.Add(self.m_textCtrl15, 0, wx.ALL, 5)

        self.m_textCtrl16 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        gSizer16.Add(self.m_textCtrl16, 0, wx.ALL, 5)

        bSizer13.Add(gSizer16, 1, wx.EXPAND, 5)

        bSizer6.Add(bSizer13, 1, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        if file:
            gSizer15 = wx.GridSizer(0, 2, 0, 0)

            self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"验证文件保存目录", wx.DefaultPosition, wx.DefaultSize, 0)
            self.m_staticText17.Wrap(-1)
            self.m_staticText17.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))
            gSizer15.Add(self.m_staticText17, 0, wx.ALL, 5)

            self.m_staticText18 = wx.StaticText(self, wx.ID_ANY, u"验证文件保存名称", wx.DefaultPosition, wx.DefaultSize, 0)
            self.m_staticText18.Wrap(-1)
            self.m_staticText18.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))
            gSizer15.Add(self.m_staticText18, 0, wx.ALL, 5)

            self.m_dirPicker3 = wx.DirPickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition,
                                                 wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
            gSizer15.Add(self.m_dirPicker3, 0, wx.ALL, 5)

            self.m_textCtrl14 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
            gSizer15.Add(self.m_textCtrl14, 0, wx.ALL, 5)

            bSizer11.Add(gSizer15, 1, wx.EXPAND, 5)

        bSizer6.Add(bSizer11, 1, wx.EXPAND, 5)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"验证", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_button4, 0, wx.ALL | wx.EXPAND, 5)

        bSizer6.Add(bSizer12, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button4.Bind(wx.EVT_BUTTON, self.de_data)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def de_data(self, event):
        c1_len = int(self.c1_len.GetValue())
        c2_len = int(self.c2_len.GetValue())
        p = int(self.m_textCtrl15.GetValue())
        x = int(self.m_textCtrl16.GetValue())

        from model import ElGamal
        if self.file:
            import os
            m_path = os.path.join(self.m_dirPicker3.GetPath(), self.m_textCtrl14.GetValue())
            path = ElGamal.data_decrypt(p=p, x=x, path1=self.c1_path, path2=self.c2_path,
                                 c1_max_len=c1_len, c2_max_len=c2_len, path_m=m_path)

            string = '验证文件存放地址为：\n' + path

        else:
            data = ElGamal.data_decrypt(p=p, x=x, path1=self.c1_path, path2=self.c2_path,
                                 c1_max_len=c1_len, c2_max_len=c2_len)
            string = data

        from Gui.ElGamal.de_result import de_Frame
        myframe = de_Frame(None, content=string)
        myframe.Show(True)
        self.__del__()
