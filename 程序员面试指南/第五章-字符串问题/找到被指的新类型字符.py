# coding=utf-8
'''
新类型字符的定义如下：
1. 新类型字符是长度为1或者2的字符串
2. 表现形式可以仅是小写字母，例如"e"；也可以是大写字母+小写字母，例如"Ab"；
还可以是大写字母+大写字母，例如"DC"
  现在给定一个字符串str，str一定是若干新类型字符正确组合的结果。比如"eaCCBi"，
由新类型字符"e"、"a"、"CC"和"Bi"拼成。再给定一个整数k，代表str中的位置。请返回
k位置指中的新类型字符。

str="aaABCDEcBCg"
1.k=7时，返回"Ec"
2.k=4时，返回"CD"
3.k=10时，返回"g"

从k-1位置开始，向左统计连续出现的大写字母的数量记为uNum，遇到小写字母就停止。
如果uNum为奇数，str[k-1...k]是被指中的新类型字符
如果uNum为偶数且str[k]是大写字母，str[k...k+1]是被指中的新类型字符
如果uNum为偶数且str[k]是小写字母，str[k]是被指中的新类型字符
'''

def pointNewChar(str, k):
    if not str or k < 0 or k >= len(str):
        return ""
    upper_num = 0
    for i in range(k-1, -1, -1):
        if not str[i].isupper():
            break
        upper_num += 1

    if upper_num & 1 == 1:
        return str[k-1: k+1]
    if str[k].isupper():
        return str[k: k+2]
    return str[k]

