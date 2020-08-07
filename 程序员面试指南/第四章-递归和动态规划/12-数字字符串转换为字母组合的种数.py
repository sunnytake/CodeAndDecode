# coding=utf-8
'''
给定一个字符串str，str全部由数字字符组成，如果str中某一个或某相邻两个字符
组成的子串值在1~26之间，则这个子串可以转换为一个字母。规定"1"转换为A，"2"
转换为"B"，"3"转换为"C"..."26"转换为"Z"。写一个函数，求str有多少种不同的
转换结果，并返回种数
'''
# 暴力递归：O(2^N)
def num1(string):
    if not string:
        return 0
    return process(string, 0)

def process(string, index):
    if index == len(string):
        return 1
    # 此时面对的是以‘0’开头的string[index:]，不可能转换
    if string[index] == '0':
        return 0
    res = process(string, index+1)
    if index+1 < len(string) and (int(string[index])*10 + int(string[index+1]) < 27):
        res += process(string, index+2)
    return res

'''
以上过程中，p(i)最多可能会有两个递归分支p(i+1)和p(i+2)，一共有N层递归。所以时间复杂度为O(2^N)
额外空间复杂度就是递归使用的函数栈的大小为O(N)。
仔细研究递归函数process：
p(i)最多依赖p(i+1)和p(i+2)，这是可以从后往前进行顺序计算的，
也就是先计算p(N)和p(N-1)，然后根据这两个值计算p(N-2)
再根据p(N-1)和p(N-2)计算p(N-3)

因为是顺序计算，所以时间复杂度为O(N)，空间复杂度为O(1)
str[i]的具体情况决定了p(i)是等于0还是等于p(i+1)，还是等于p(i+1)+p(i+2)
'''
def num2(string):
    if not string:
        return 0
    cur = 0 if string[-1] == '0' else 1
    next = 1
    for i in range(len(string)-2, -1, -1):
        if string[i] == '0':
            next = cur
            cur = 0
        else:
            temp = cur
            if int(string[i])*10 + int(string[i+1]) < 27:
                cur += next
                next = temp
    return cur

































