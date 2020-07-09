#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 9:16
# @Author  : 李金哲
# @Site    : 
# @File    : common.py
# @Software: PyCharm

def fastExpMod(m, e, n):
    """
    快速幂取模法 / 模的重复平方法
    m^e mod n
    :param m: 底数
    :param e: 幂数
    :param n: 模数
    :return: 模的结果
    """
    result = 1
    while e != 0:
        if (e & 1) == 1:
            # ei = 1, then mul
            result = (result * m) % n
        e >>= 1
        # b, b^2, b^4, b^8, ... , b^(2^n)
        m = (m * m) % n
    return result


def list_split(items, n):
    return [items[i:i + n] for i in range(0, len(items), n)]


def makefile(path, content):
    """
    以二进制编码，保存文件
    :param path: 保存地址
    :param content:  二进制数据列表
    :return:
    """
    try:
        f = open(path, 'wb')
        for i in content:
            f.write(int(i).to_bytes(1,'little'))
        f.seek(0)
        f.close()
        print('文件已生成')
    except Exception as e:
        print('错误：',e)
        exit(0)

def get_data(path):
    """
    读取文件的数据
    :param path: 文件地址
    :return: 二进制列表
    """
    f = open(path, 'rb')
    data_all = f.read()
    f.close()
    return data_all


def standard_data(data_all, lenth):
    import math
    data_list = ''
    for data in data_all:
        if data == 0:
            long = 1
        else:
            long = int(math.log10(data)) + 1
        data_list += str(long * 10 ** 3 + data)
    if lenth < 4:
        lenth = 1
    else:
        lenth = int(lenth / 4 - 1)*4
    return list_split(data_list, lenth)


def recovery_data(res):
    res = list_split(res, 4)
    m = []
    for data in res:
        lenth = int(int(data) / 1000)
        m.append(int(data) % 10 ** lenth)
    return m


def save_ctext(path, data_list, max_lenth):
    """
    签名专属写入操作 要规范数据格式，将所以数据长度一致化
    :param path: 签名存储地址
    :param data_list: 签名列表
    :param max_lenth: 单列签名最大长度
    :return: 无
    """
    m_s = ''
    for data in data_list:
        # 规范数据长度
        if len(str(data)) < max_lenth:
            m_s += '0' * (max_lenth - len(str(data))) + str(data)
        else:
            m_s += str(data)
    m_s = list_split(m_s, 2)

    makefile(path, m_s)
