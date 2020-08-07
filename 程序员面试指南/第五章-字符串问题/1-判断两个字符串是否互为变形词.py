# coding=utf-8
'''
给定两个字符串str1和str2，如果str1和str2中出现的字符种类一样且每种字符出现的次数也一样，
那么str1和str2互为变形词，请实现函数判断两个字符串是否互为变形词

字符的编码值在0-255
'''
def isDeformation(str1, str2):
    if not str1 or not str2 or len(str1) != len(str2):
        return False
    chars = [0] * 256
    for char in str1:
        chars[ord(char)] += 1
    for char in str2:
        if chars[ord(char)] == 0:
            return False
        chars[ord(char)] -= 1
    return True


























