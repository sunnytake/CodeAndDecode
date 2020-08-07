# coding=utf-8
'''
给定两个字符串str1和str2，返回两个字符串的最长公共子序列
str1 = "1A2C3D4B56"
str2 = "B1D23CA45B6A"
"123456"或者"12C4B6"都是最长公共序列

两个字符串的最长公共子串与最长公共子序列的区别：
最长公共子串要求在原字符串中是连续的，而子序列只需要保持相对顺序一致，并不要求连续。

dp[i][j]表示str1[0...i]与str2[0...j]的最长公共子序列的长度
'''

# 计算dp矩阵的时间复杂度为O(M*N)，通过dp得到最长公共子序列为O(M+N)
def getdp(str1, str2):
    dp = []
    for i in range(len(str1)):
        dp.append([0]*len(str2))
    if str1[0] == str2[0]:
        dp[0][0] = 1
    # 列初始化
    for i in range(1, len(str1)):
        temp = 1 if str1[i] == str2[0] else 0
        dp[i][0] = max(dp[i-1][0], temp)
    # 行初始化
    for i in range(1, len(str2)):
        temp = 1 if str1[0] == str2[i] else 0
        dp[0][i] = max(dp[0][i-1], temp)
    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if str1[i] == str2[j]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
    return dp

# 通过dp求解最长公共子序列
def process(str1, str2):
    if not str1 or not str2:
        return ""
    dp = getdp(str1, str2)
    len1, len2 = len(str1)-1, len(str2)-1
    res = ""
    count = dp[-1][-1]
    while count > 0:
        if len2 > 0 and dp[len1][len2] == dp[len1][len2-1]:
            len2 -= 1
        elif len1 > 0 and dp[len1][len2] == dp[len1-1][len2]:
            len1 -= 1
        else:
            res = str1[len1] + res
            len1 -= 1
            len2 -= 1
            count -= 1
    return res

if __name__ == '__main__':
    str1 = "1A2C3D4B56"
    str2 = "B1D23CA45B6A"
    print(process(str1, str2))