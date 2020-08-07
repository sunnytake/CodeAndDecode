# coding=utf-8

'''
原问题：给定整数N，返回斐波那契数列的第N项
'''

# 原问题：暴力递归，时间复杂度O(N^2)
def fib1(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    return fib1(n-1) + fib1(n-2)

# 原问题：依次计算各项，时间复杂度O(N)
def fib2(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    pre = 1
    res = 1
    for i in range(3, n+1):
        tmp = res
        res += pre
        pre = tmp
    return res

'''
扩展问题1：给定整数N，代表台阶数，一次可以跨2个或者1个台阶，返回有多少种走法
'''
# 扩展问题1：暴力递归，时间复杂度O(N^2)
def topo1(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return n
    return topo1(n-1) + topo1(n-2)

# 扩展问题1：依次计算各项，时间复杂度O(N)
def topo2(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return n
    res = 2
    pre = 1
    for i in range(3, n+1):
        tmp = res
        res += pre
        pre = tmp
    return res

'''
扩展问题2:
假设农场中成熟的母牛每年只会生1头小母牛，并且永远不会死。第一年农场有1只成熟的母牛，
从第二年开始，母牛开始生小母牛。每只小母牛3年之后成熟又可以生小母牛。给定整数N，求出
N年后牛的数量。
0年      1年      2年          3年
0        0        0            1               == 第1年
1        0        0            1               == 第2年
1        1        0            1               == 第3年
1        1        1            1               == 第4年
'''
def niu1(n):
    if n < 1:
        return 0
    if n == 1 or n == 2 or n == 3:
        return n
    return niu1(n-1) + niu1(n-2)

def niu2(n):
    if n < 1:
        return 0
    if n == 1 or n == 2 or n == 3:
        return n
    res = 3
    pre, prepre = 2, 1
    for i in range(4, n+1):
        temp1, temp2 = res, pre
        res += prepre
        pre, prepre = temp1, temp2
    return res



























































