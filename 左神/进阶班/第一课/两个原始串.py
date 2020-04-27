# coding=utf-8
"""
利用已有字符串向后添加字符，最终生成的字符串包含两个原始串，两个原始串开始位置不一样，求这样的最短串
eg: abcabc
添加后：abcabcabc
思路：算出整体串的最长前缀和最长后缀(nexts数组)，追加中间的部分
"""
def generateTwoStr(string):
    nexts = getNexts(string)
    return string + string[nexts[-1]:]

def getNexts(pattern):
    if len(pattern) == 1:
        return [-1]
    nexts = [0]*len(pattern)
    nexts[0] = -1
    cur = 0
    index = 2
    while index < len(pattern):
        if pattern[index] == pattern[cur]:
            cur += 1
            nexts[index] = cur
            index += 1
        elif cur > 0:
            cur = nexts[cur]
        else:
            nexts[index] = 0
            index += 1
    return nexts

if __name__ == '__main__':
    string = "abcabc"
    print(generateTwoStr(string))