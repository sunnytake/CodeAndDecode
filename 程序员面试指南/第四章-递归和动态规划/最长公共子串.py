# coding=utf-8
'''
给定两个字符串str1和str2，返回两个字符串的最长公共子串
str1 = "1AB2345CD", str2="12345EF"，返回"2345"

dp[i][j]：把str1[i]和str2[j]当作公共子串最后一个字符的情况下
'''
def getdp(str1, str2):
    dp = []
    for i in range(len(str1)):
        dp.append([0]*len(str2))
    # 列初始化
    for i in range(len(str1)):
        if str1[i] == str2[0]:
            dp[i][0] = 1
    # 行初始化
    for j in range(len(str2)):
        if str1[0] == str2[j]:
            dp[0][j] = 1

    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
    return dp

def process(str1, str2):
    if not str1 or not str2:
        return ""
    dp = getdp(str1, str2)
    max = 0
    end = None
    for i in range(len(str1)):
        for j in range(len(str2)):
            if dp[i][j] > max:
                end = i
                max = dp[i][j]
    return str1[end-max+1: end+1]