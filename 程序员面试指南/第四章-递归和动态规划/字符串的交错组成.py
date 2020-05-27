# coding=utf-8
'''
给定三个字符串str1、str2和aim。如果aim包含且仅包含来自str1和str2的所有字符，
而且在aim中属于str1的字符之间保持原来在str1中的顺序，属于str2的字符之间保持
原来在str2中的顺序，那么称aim是str1和str2的交错组成。实现一个函数，判断aim
是否由str1和str2交错组成。

str1="AB"，str2="12"。那么"AB12"、"A1B2"、"A12B"、"1A2B"和"1AB2"等都是str1和str2的交错组成
dp[i][j]代表aim[0...i+j-1]是否被str1[0...i-1]和str2[0...j-1]交错组成
'''
def isCross1(str1, str2, aim):
    if not str1 or not str2 or not aim:
        return False
    if len(str1) + len(str2) != len(aim):
        return False
    dp = []
    for i in range(len(str1)+1):
        dp.append([False]*(len(str2)+1))
    dp[0][0] = True
    # 行初始化
    for i in range(len(str1)+1):
        if str1[i-1] != aim[i-1]:
            break
        dp[i][0] = True
    # 列初始化
    for j in range(len(str2)+1):
        if str2[j-1] != aim[j-1]:
            break
        dp[0][j] = True
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if (dp[i-1][j] and str1[i-1] == aim[i+j-1]) or (dp[i][j-1] and str2[j-1] == aim[i+j-1]):
                dp[i][j] = True
    return dp[-1][-1]

def isCross2(str1, str2, aim):
    if not str1 or not str2 or not aim:
        return False
    if len(str1) + len(str2) != len(aim):
        return False
    if len(str1) >= len(str2):
        long_str, short_str = str1, str2
    else:
        long_str, short_str = str2, str1
    dp = [True] + [False]*len(short_str)
    for i in range(1, len(short_str)+1):
        if short_str[i-1] == aim[i-1]:
            break
        dp[i] = True

    for i in range(1, len(long_str)+1):
        dp[0] = dp[0] and long_str[i-1] == aim[i-1]
        for j in range(1, len(short_str)+1):
            if (long_str[i-1] == aim[i+j-1] and dp[j]) or (short_str[j-1] == aim[i+j-1] and dp[j-1]):
                dp[j] = True
            else:
                dp[j] = False
    return dp[-1]



























