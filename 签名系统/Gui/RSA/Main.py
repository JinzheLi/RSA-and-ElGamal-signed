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
## Class RSA_main
###########################################################################

class RSA_main(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(613, 573), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetBackgroundColour('#f0d05b')

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"RSA数字签名系统", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(22, 70, 90, 90, False, "宋体"))

        bSizer2.Add(self.m_staticText1, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"大质数p的长度", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        self.m_staticText4.SetFont(wx.Font(14, 70, 90, 90, False, "宋体"))

        gSizer1.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"大质数q的长度", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        self.m_staticText5.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

        gSizer1.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.p_len = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(250, -1), 0)
        gSizer1.Add(self.p_len, 0, wx.ALL, 5)

        self.q_len = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(250, -1), 0)
        gSizer1.Add(self.q_len, 0, wx.ALL, 5)

        bSizer3.Add(gSizer1, 1, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"生成密钥(两个质数的长度和应当大于2)", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_button1, 0, wx.ALL, 5)

        bSizer3.Add(bSizer4, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer3, 1, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"签名模块", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        self.m_staticText10.SetFont(wx.Font(16, 70, 90, 90, False, "宋体"))

        bSizer5.Add(self.m_staticText10, 0, wx.ALL, 5)

        gSizer2 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"数据签名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        self.m_staticText6.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

        gSizer2.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"文档签名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        self.m_staticText7.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

        gSizer2.Add(self.m_staticText7, 0, wx.ALL, 5)

        self.m_text = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(250, -1), 0)
        gSizer2.Add(self.m_text, 0, wx.ALL, 5)

        self.m_file = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition,
                                        wx.Size(250, -1), wx.FLP_DEFAULT_STYLE)
        gSizer2.Add(self.m_file, 0, wx.ALL, 5)

        m_comboBox1Choices = [u"文档签名", u"数据签名"]
        self.m_comboBox1 = wx.ComboBox(self, wx.ID_ANY, m_comboBox1Choices[0], wx.DefaultPosition, wx.Size(250, -1),
                                       m_comboBox1Choices, wx.TE_READONLY)
        gSizer2.Add(self.m_comboBox1, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"签名操作", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_button2, 0, wx.ALL, 5)

        bSizer5.Add(gSizer2, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer5, 1, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"验证模块", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        self.m_staticText11.SetFont(wx.Font(16, 70, 90, 90, False, "宋体"))

        bSizer6.Add(self.m_staticText11, 0, wx.ALL, 5)

        gSizer4 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, u"签名地址", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        self.m_staticText12.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

        gSizer4.Add(self.m_staticText12, 0, wx.ALL, 5)

        self.m_filePicker4 = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
                                               wx.DefaultPosition, wx.Size(250, -1), wx.FLP_DEFAULT_STYLE)
        gSizer4.Add(self.m_filePicker4, 0, wx.ALL, 5)

        m_comboBox3Choices = [u"文档验证", u"数据验证"]
        self.m_comboBox3 = wx.ComboBox(self, wx.ID_ANY, m_comboBox3Choices[0], wx.DefaultPosition, wx.Size(250, -1),
                                       m_comboBox3Choices, wx.TE_READONLY)
        gSizer4.Add(self.m_comboBox3, 0, wx.ALL, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"验证操作", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.m_button4, 0, wx.ALL, 5)

        bSizer6.Add(gSizer4, 1, wx.EXPAND, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"返回主菜单", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_button5, 0, wx.ALL, 5)

        bSizer1.Add(bSizer6, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button1.Bind(wx.EVT_BUTTON, self.get_key)
        self.m_button2.Bind(wx.EVT_BUTTON, self.en_data)
        self.m_button4.Bind(wx.EVT_BUTTON, self.de_data)
        self.m_button5.Bind(wx.EVT_BUTTON, self.return_menu)

    def __del__(self):
        self.Destroy()

    # Virtual event handlers, overide them in your derived class
    def get_key(self, event):
        if int(self.p_len.GetValue()) + int(self.q_len.GetValue()) > 2:
            from Gui.RSA.key_result import key_result
            myframe = key_result(None, p_len=int(self.p_len.GetValue()), q_len=int(self.q_len.GetValue()))
            myframe.Show(True)

    def en_data(self, event):
        from Gui.RSA.en_data import en_data
        if self.m_comboBox1.GetValue() == '文档签名':
            if self.m_file.GetPath():
                myframe = en_data(None, path=self.m_file.GetPath())
                myframe.Show(True)
        if self.m_comboBox1.GetValue() == '数据签名':
            if self.m_text.GetValue():
                myframe = en_data(None, m=self.m_text.GetValue())
                myframe.Show(True)

    def de_data(self, event):
        from Gui.RSA.de_data import de_data
        if self.m_comboBox3.GetValue() == '文档验证':
            file = True
        else:
            file = False
        if self.m_filePicker4.GetPath():
            myframe = de_data(None, path=self.m_filePicker4.GetPath(), file=file)
            myframe.Show(True)

    def return_menu(self, event):
        self.__del__()
        from Gui.enter import MyFrame2
        SiteFrame = MyFrame2(None)
        SiteFrame.Show()
