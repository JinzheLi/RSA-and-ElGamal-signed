#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 18:26
# @Author  : 李金哲
# @Site    : 
# @File    : ElGamal.py
# @Software: PyCharm

from model.common import fastExpMod, list_split, makefile, get_data, standard_data, recovery_data, save_ctext


def get_key(n=20):
    """
    获取公钥 p, g , (g^x)mod p 和私钥 x
    :param n: the long of random prime
    :return: p,g,y,x
    """
    import pyunit_prime
    p = pyunit_prime.get_large_prime_length(n)
    # p = 49924286347363285385002602166419178756593347008815637398138749880304666805251999
    yn = p - 1
    f = 2
    x_list = []
    while yn != 1:
        print('yn：', yn)
        print('f：', f)
        print(pyunit_prime.is_prime(int(yn)))
        if pyunit_prime.is_prime(int(yn)):
            x_list.append(int(yn))
            break
        if pyunit_prime.is_prime(f):
            if yn % f == 0:
                x_list.append(f)
                while yn % f == 0:
                    yn = yn // f
            if yn == 1:
                break
            f += 1
        else:
            f += 1

    yn = p - 1
    print('yn：', yn)
    print('x list：', x_list)
    error_list = []
    import random
    while True:
        i = random.randint(2, p)
        if i in error_list:
            continue
        else:
            error_list.append(i)
        k = 0
        for j in x_list:
            if fastExpMod(i, int(yn // j), p) == 1:
                break
            else:
                k += 1
        if k == len(x_list):
            import random
            x = random.randint(1, p - 1)

            return p, i, fastExpMod(i, x, p), x


def exgcd(a, b, x=1, y=0):
    # 当b=0的时候return
    if b == 0:
        return a, x, y
    # 递归调用，获取b, a%b时的gcd与通项解
    gcd, x, y = exgcd(b, a % b, x, y)
    # 代入，得到新的通项解
    x, y = y, x - a // b * y
    return gcd, x, y


def cal_inv(a, m):
    """
    求逆元
    :param a: x
    :param m: 模的值
    :return: x对m的逆元
    """
    gcd, x, y = exgcd(a, m)
    # 如果gcd不为1，那么说明没有逆元，返回-1
    return (x % m + m) % m if gcd == 1 else -1


def encrypt(m, p, g, y):
    """
    加密操作
    c1 = g^k mod p
    c2 = m*y^k mod p
    :param m: 加密信息
    :param p:   公开参数
    :param g:   公开参数
    :param y:   公开参数(g^x mod p)
    :return: 密文c1和c2
    """
    import random
    while True:
        k = random.randint(1, p - 1)
        if exgcd(k, p - 1)[0] == 1:
            break
    c1 = fastExpMod(g, k, p)
    c = fastExpMod(y, k, p)
    c2 = m * c % p
    return c1, c2


def decrypt(c1, c2, x, p):
    """
    解密
    m = c2 * (c1^x)^(-1) mod p
    :param c1: 密文
    :param c2: 密文
    :param x:  私钥 x
    :param p: 公钥p
    :return: 明文 m
    """
    c1 = fastExpMod(c1, x, p)
    c1 = cal_inv(c1, p)
    return c1 * c2 % p


def data_encrypt(p, g, y, c_path, path=None, m_data=None):
    """
    明文加密程序
    :return: 无
    """
    # path = input('请输入要加密的文档位置')
    # path = './dota_radar.JPG'
    if path:
        data = get_data(path)
    else:
        data = m_data.encode()
    print(data)
    import math
    data_list = standard_data(data, lenth=int(math.log10(p))+1)

    c1_l = []
    c2_l = []
    c1_max_len = 0
    c2_max_len = 0
    # 加密明文，并获取密文最大长度
    for data in data_list:
        num = int(data)
        c1, c2 = encrypt(num, p, g, y)
        c1_l.append(c1)
        c2_l.append(c2)
        if c1 != 0:
            len1 = int(math.log10(c1)) + 1
        else:
            len1 = 1
        if c2 != 0:
            len2 = int(math.log10(c2)) + 1
        else:
            len2 = 1
        if len1 > c1_max_len:
            c1_max_len = int(math.log10(c1)) + 1
        if len2 > c2_max_len:
            c2_max_len = int(math.log10(c2)) + 1

    # path = str(input('密文 C1 的存储地址：'))
    import os
    path1 = os.path.join(c_path, 'c1.txt')
    save_ctext(path1, c1_l, c1_max_len)
    # path = str(input('密文 C2 的存储地址：'))
    path2 = os.path.join(c_path, 'c2.txt')
    save_ctext(path2, c2_l, c2_max_len)
    return path1, path2, c1_max_len, c2_max_len


def data_decrypt(p, x, path1, path2, c1_max_len, c2_max_len, path_m=None):
    """
    数据解密函数
    :return: 无
    """
    c1 = get_data(path1)
    import math
    m_list = ''
    lenth = 0
    for m in c1:
        lenth += 1
        if lenth == len(c1):
            m_list += str(m)
        elif m == 0:
            m_list += '00'
        else:
            m_list += '0' * (1 - int(math.log10(m))) + str(m)
    c1 = m_list
    # path = input('请输入密文2地址：')
    # path = './c2.txt'
    c2 = get_data(path2)

    import math
    m_list = ''
    lenth = 0
    for m in c2:
        lenth += 1
        if lenth == len(c2):
            m_list += str(m)
        elif m == 0:
            m_list += '00'
        else:
            m_list += '0' * (1 - int(math.log10(m))) + str(m)
    c2 = m_list

    c1 = list_split(c1, c1_max_len)
    if len(c1[len(c1) - 1]) < c1_max_len:
        c1[len(c1) - 1] += c1[len(c1) - 1][len(c1[len(c1) - 1]) - 1]
        c1[len(c1) - 1][len(c1[len(c1) - 1]) - 1] = '0'
    c2 = list_split(c2, c2_max_len)
    if len(c2[len(c2) - 1]) < c2_max_len:
        c2[len(c2) - 1] += c2[len(c2) - 1][len(c2[len(c2) - 1]) - 1]
        c2[len(c2) - 1][len(c2[len(c2) - 1]) - 1] = '0'

    if len(c1) != len(c2):
        print('密文有错误')
        exit(0)

    res = ''
    for i in range(len(c1)):
        res += str(decrypt(int(c1[i]), int(c2[i]), x, p))

    m = recovery_data(res)

    # path = input('请输入保存地址和文件名字')
    # path = './111.JPG'
    if path_m:
        makefile(path_m, m)
        return path_m
    else:
        m_s = bytes()
        print(m)
        for data in m:
            print(data)
            m_s += int(data).to_bytes(1, 'little')

        return m_s.decode()
