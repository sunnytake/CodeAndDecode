# coding=utf-8
'''
给定一个字符串str，返回把str全部切成回文子串的最小分割数

str = "ABA"。不需要切割，str本身就是回文串，所以返回0
str="ACDCDCDAD"，最少需要切2次变成3个回文子串，比如"A"、"CDCDC"和"DAD"，所以返回2

dp[i]表示str[i...len-1]至少需要切割几次，才能把str[i...len-1]全部切成回文子串。则dp[0]即为最后结果
从右往左依次计算dp[i]的值，i初始为len-1，具体计算过程如下：
1. 假设j位置
'''
def minCut(str):
    if not str:
        return 0
    dp = [len(str)]*(len(str)+1)
    dp[len(str)] = -1

    p = []
    for i in range(len(str)):
        p.append([0]*len(str))

    for i in range(len(str)-1, -1, -1):
        for j in range(i, len(str)):
            if str[i] == str[j] and (j-i<2 or p[i+1][j-1]):
                p[i][j] = True
                dp[i] = min(dp[i], dp[j+1]+1)
    return dp[0]

















