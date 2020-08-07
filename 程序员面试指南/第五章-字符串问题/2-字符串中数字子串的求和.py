# coding=utf-8
'''
给定一个字符串str，求其中全部数字串所代表的数字之和
1.忽略小数点字符。例如"A1.3"，其中包含两个数字1和3
2.如果紧贴数字子串的左侧出现字符"-"，当连续出现的数量为奇数时，则数字视为负数，
连续出现的数量为偶数时，则数字为正。例如, "A-1BC--12"，其中包含数字为-1和12
str="A1CD2E33" => 36
str="A-1B--2C--D6E" => 7
'''
# 方法1：借助栈
def numSum(str):
    if not str:
        return 0
    res = 0
    stack = []
    index = 0
    while index < len(str) or stack:
        char = str[index] if index < len(str) else None

        if char and '0' <= char <= '9':
            stack.append(char)
        else:
            if char and char == '-':
                stack.append(char)
            else:
                flag = True # 符号
                val = 0 # 数值
                while stack:
                    temp = stack.pop(0)
                    if '0' <= temp <= '9':
                        val = val*10 + ord(temp) - ord('0')
                    else:
                        flag = not flag
                if flag:
                    res += val
                else:
                    res -= val
        index += 1
    return res

# 方法2：牛批
def numSum(str):
    if not str:
        return 0
    res = 0
    pos = True
    num = 0
    for index, char in enumerate(str):
        if char < '0' or char > '9':
            res += num
            if char == '-':
                if index-1 > -1 and str[index-1] == '-':
                    pos = not pos
                else:
                    pos = False
            else:
                pos = True
        else:
            num = num * 10
            if pos:
                num += ord(char) - ord('0')
            else:
                num += - (ord(char) - ord('0'))
    res += num
    return res