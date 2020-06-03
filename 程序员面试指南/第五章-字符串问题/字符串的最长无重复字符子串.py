# coding=utf-8
'''
给定一个字符串str，返回str的最长无重复字符子串的长度

str="abcd"，返回4
str="aabcb"，最长无重复字符子串为"abc"，返回3
'''
def maxUnique(str):
    if not str:
        return 0
    map = [-1] * 256
    # pre+1表示在必须以str[i-1]结尾的情况下，最长无重复字符子串的开始位置
    pre = -1
    length = 0
    for index, char in enumerate(str):
        pre = max(pre, map[char])
        cur = index - pre
        length = max(length, cur)
        map[char] = index
    return length
