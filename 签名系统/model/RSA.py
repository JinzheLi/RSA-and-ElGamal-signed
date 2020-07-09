#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 11:33
# @Author  : 李金哲
# @Site    : 
# @File    : RSA.py
# @Software: PyCharm

from model.common import fastExpMod, list_split, makefile, get_data, standard_data, recovery_data, save_ctext


def get_two_prime(lenth1, lenth2):
    """
    获取两个大素数
    :param lenth1 >=2:
    :param lenth2 >=2:
    :return:大素数1和大素数2， 长度为lenth1和lenth2，默认值为512
    """
    from pyunit_prime import prime

    prime1 = prime.get_large_prime_length(lenth1)
    prime2 = prime.get_large_prime_length(lenth2)
    while prime1 == prime2:
        prime2 = prime.get_large_prime_length(lenth2)

    return prime1, prime2


def ext_gcd(a, b):  # 扩展欧几里得算法
    if b == 0:
        return 1, 0, a
    else:
        x, y, gcd = ext_gcd(b, a % b)  # 递归直至余数等于0(需多递归一层用来判断)
        x, y = y, (x - (a // b) * y)  # 辗转相除法反向推导每层a、b的因子使得gcd(a,b)=ax+by成立
        return x, y, gcd


def get_key(len1, len2):
    """
    公开的n,e和私钥d
    :param len1: 大质数1的长度
    :param len2: 大质数2的长度
    :return: 公开的n, e, d
    """
    p, q = get_two_prime(len1, len2)
    n = p * q
    yn = (p - 1) * (q - 1)

    import random
    while True:
        e = random.randint(2, yn)
        res = ext_gcd(e, yn)
        if res[2] == 1:
            break
    if res[1] < 0:
        d = yn + res[1]
    else:
        d = res[1]
    return n, e, d


def data_encrypt(n, e, c_path, path=None, m=None):
    # path = input('请输入你的文档路径:')
    #   D:\Workspaces\python_练习\密码学\test1.py
    if path:
        data_all = get_data(path)
    else:
        data_all = m.encode()
    # n = int(input('请输入公开参数n：\t'))
    # e = int(input('请输入公开参数e：\t'))

    import math

    data_list = standard_data(data_all, lenth=int(math.log10(n)) + 1)
    m_l = []
    max_len = 0

    for data in data_list:
        c = fastExpMod(int(data), e, n)
        if c == 0:
            lenth = 1
        else:
            lenth = int(math.log10(c)) + 1
        if lenth > max_len:
            max_len = lenth
        m_l.append(c)

    save_ctext(c_path, m_l, max_len)
    return c_path, max_len

def data_decrypt(n, d, c_max_len, c_path, m_path=None):

    c = get_data(c_path)
    import math
    m_list = ''
    lenth = 0
    for m in c:
        lenth += 1
        if lenth == len(c):
            m_list += str(m)
        elif m == 0:
            m_list += '00'
        else:
            m_list += '0' * (1 - int(math.log10(m))) + str(m)
    
    c = m_list
    c = list_split(c, c_max_len)
    if len(c[len(c) - 1]) < c_max_len:
        c[len(c) - 1] += c[len(c) - 1][len(c[len(c) - 1]) - 1]
        c[len(c) - 1][len(c[len(c) - 1]) - 1] = '0'
    res = ''
    
    for data in c:
        m = fastExpMod(int(data), d, n)
        res += str(m)

    m = recovery_data(res)

    if m_path:
        makefile(m_path, m)
        return m_path
    else:
        m_s = bytes()
        for data in m:
            m_s += data.to_bytes(1, 'little')
        return m_s.decode()
