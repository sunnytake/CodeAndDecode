# coding=utf-8
'''
给定一个字符串str，返回str的统计字符串，
例如"aaabbadddffc"的统计字符串为"a_3_b_2_a_1_d_3_f_2_c_1"

进阶:
给定一个字符串的统计字符串cstr，再给定一个整数index，返回cstr所代表的原始字符串上
的第index个字符。例如，"a_1_b_100"所代表的原始字符串上第0个字符是'a'，第50个字符
是'b'
'''
def getCountString(str):
    if not str:
        return ""
    num = 1
    res = str[0]
    for i in range(1, len(str)):
        if str[i] != str[i-1]:
            res = concat(res, num, str[i])
            num = 1
        else:
            num += 1
    return concat(res, num, "")

def concat(res, num, char):
    if char:
        return res + "_" + str(num) + "_" + char
    else:
        return res + "_" + str(num)

# 进阶
def getCharAt(cstr, index):
    if not cstr:
        return 0
    sum_val, num = 0, 0
    cur = None
    # True为字符阶段，False为数字
    stage = True
    for i, char in enumerate(cstr):
        if char == '_':
            stage = not stage
        elif stage:
           sum_val += num
           if sum_val > index:
               return cur
           num = 0
           cur = char
        else:
            num = num * 10 + ord(char) - ord('0')
    if sum_val + num > index:
        return cur
    return None














