# coding=utf-8
'''
给定一个字符串str，判断是不是整体有效的括号字符串

str=""，返回true；
str="(()())"，返回true;
str="(())"，返回true
str="())"，返回false
str="()("，返回false
str="()a()"，返回false
'''
def isValid(str):
    if not str:
        return False
    status = 0
    for i in range(len(str)):
        if str[i] != ')' and str[i] != '(':
            return False
        if str[i] == ')' and status < 1:
            return False
        if str[i] == '(':
            status += 1
    return status == 0


'''
进阶：给定一个括号字符串str，返回最长的有效括号子串

str="(()())"，返回6
str="())"，返回2
str="()(()()("，返回4

动态规划，时间复杂度为O(N)，额外空间复杂度为O(N)
dp[i]表示str[0...i]种必须以str[i]结尾的最长的有效括号子串长度
'''
def maxLength(str):
    if not str:
        return 0
    dp = [0] * len(str)
    res = 0
    for i in range(1, len(str)):
        if str[i] == ')':
            pre = i - dp[i-1] - 1
            if pre >= 0 and str[pre] == '(':
                dp[i] = dp[i-1] + 2
                if pre > 0:
                    dp[i] += dp[pre-1]
            res = max(res, dp[i])
    return res