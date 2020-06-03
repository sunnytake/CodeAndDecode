# coding=utf-8
'''
给定一个字符串str，如果可以在str的任意位置添加字符，请返回在添加字符最少的情况下，
让str整体都是回文字符串的一种结果。

str="ABA"，str本身就是回文串，不需要添加字符，所以返回"ABA"
str="AB"，可以在'A'之前添加'B'，使str整体都是回文串。故可以返回"BAB"。
也可以在'B'之后添加'A'，使str整体都是回文串，故也可以返回"ABA"。总之，
只要添加的字符数最少，只返回其中一种结果即可

dp[i][j]：子串str[i...j]最少添加几个字符可以使str[i...j]整体都是回文串。
* 如果str[i...j]只有一个字符，dp[i][j]=
* 如果str[i...j]有两个字符
    如果两个字符相等，dp[i][j]=0
    如果不等，dp[i][j]=1
* 如果str[i...j]有多个字符
    如果str[i]==str[j]，那么dp[i][j]=dp[i+1][j-1]
    如果str[i]!=str[j]，要让str[i...j]整体变为回文串有两种方法：
        1.让str[i...j-1]先变成回文串，然后在左边加上字符str[j]
        2.让str[i+1...j]先变成回文串，然后在右边加上字符str[i]
    即dp[i][j] = min(dp[i][j-1], dp[i+1][j])
'''
def getDp(str):
    dp = []
    for i in range(len(str)):
        dp.append([0]*len(str))
    for j in range(1, len(str)):
        # 两个字符
        dp[j-1][j] = 0 if str[j-1] == str[j] else 1
        # 多个字符
        for i in range(j-2, -1, -1):
            if str[i] == str[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
    return dp

# 求dp矩阵时间复杂度为O(N^2),根据str和dp求解最终结果为O(N)，所以原问题时间复杂度为O(N^2)
def getPalindrome1(str):
    if not str or len(str) < 2:
        return str
    dp = getDp(str)
    res = [None] * (len(str) + dp[0][len(str)-1])
    i, j = 0, len(str)-1
    resl, resr = 0, len(str) + dp[0][len(str)-1] - 1
    while i <= j:
        if str[i] == str[j]:
            res[resl] = str[i]
            resl += 1
            i += 1
            res[resr] = str[j]
            resr -= 1
            j -= 1
        elif dp[i][j-1] < dp[i+1][j]:
            res[resl] = str[j]
            resl += 1
            res[resr] = str[j]
            resr -= 1
            j -= 1
        else:
            res[resl] = str[i]
            resl += 1
            res[resr] = str[i]
            resr -= 1
            i += 1
    return ''.join(res)


'''
进阶：给定一个字符串str，再给定str的最长回文子序列字符串strlps，请返回在添加
字符最少的情况下，让str整体都是回文字符串的一种结果。

str="A1B21C"，strlps="121"，返回"AC1B2B1CA"或者"CA1B2B1AC"。
'''
def getPalindrome2(str, strlps):
    if not str:
        return ""
    res = [None] * (len(str)*2 - len(strlps))
    left1, right1 = 0, len(str)-1
    left2, right2 = 0, len(strlps)-1
    res_left, res_right = 0, len(str)*2 - len(strlps)-1
    while left2 <= right2:
        temp_left, temp_right = left1, right1
        while str[left1] != strlps[left2]:
            left1 += 1
        while str[right1] != strlps[right2]:
            right1 -= 1
        set(res, res_left, res_right, str, temp_left, left1, right1, temp_right)
        res_left += left1 - temp_left + temp_right - right1
        res_right -= left1 - temp_left + temp_right - right1
        res[res_left] = str[left1]
        res_left += 1
        left1 += 1
        res[res_right] = str[right1]
        res_right -= 1
        right1 -= 1
        left2 += 1
        right2 += 1
    return ''.join(res)

def set(res, res_left, res_right, str, left_start, left_end, right_start, right_end):
    for i in range(left_start, left_end):
        res[res_left] = str[i]
        res_left += 1
        res[res_right] = str[i]
        res_right -= 1
    for i in range(right_end, right_start, -1):
        res[res_left] = str[i]
        res_left += 1
        res[res_right] = str[i]
        res_right -= 1

























