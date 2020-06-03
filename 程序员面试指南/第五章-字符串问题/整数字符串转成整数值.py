# coding=utf-8
'''
给定一个字符串str，如果str符合日常书写的整数形式，并且属于32位整数的范围，
返回str所代表的整数值，否则返回0

str="123"，返回123
str="023"，因为"023"不符合日常的书写习惯，所以返回0
str="A13"，返回0
str="0"，返回0
str="2147483647"，返回2147483647
str="2147483648"，因为溢出了，所以返回0
str="-123"，返回-123
'''
def isValid(str):
    if str[0] != '-' and (str[0] < '0' or str[0] > '9'):
        return False
    if str[0] == '-' and (len(str) == 1 or str[1] == '0'):
        return False
    if str[0] == '0' and len(str) > 1:
        return False
    for char in str[1:]:
        if char < '0' or char > '9':
            return False
    return True

def conver(str):
    if not str:
        return 0
    if not isValid(str):
        return 0
    pos = True
    res = 0
    for index, char in enumerate(str):
        if index == 0:
            if char == '-':
                pos = not pos
            else:
                return 0
        else:
            res = res*10 + ord(char) - ord('0')
    return -res if not pos else res


















