# coding=utf-8
'''
给定一个整数N，求由"0"字符与"1"字符组成的长度为N的所有字符串中，
满足"0"字符的左边必有"1"字符的字符串数量

N=1,只有1符合
N=2，10和11符合
N=3，101、110和111符合
'''
# 暴力递归，时间复杂度O(2^N)
def getNum1(n):
    if n < 1:
        return 0
    return process(1, n)

def process(i, n):
    if i == n-1:
        return 2
    if i == n:
        return 1
    return process(i+1, n) + process(i+2, n)

# 时间复杂度O(N)，空间复杂度O(1)
def getNum2(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    pre = 1
    cur = 1
    for i in range(2, n+1):
        temp = cur
        cur += pre
        pre = temp
    return cur





















