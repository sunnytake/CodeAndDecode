# coding=utf-8
"""
给定长度为m的字符串aim，以及一个长度为n的字符串str
请问能否在str中找到一个长度为m的连续子串，使得这个子串刚好由aim的m个字符组成顺序无所谓，
返回任意满足条件的一个子串的起始位置，未找到返回-1

同源异构词："abcd", "bdca"
1). 排序后相同
2).利用ascii码0-255，共266个
"""
def isCountEqual(string, start, aim):
    chars = [0]*256
    for char in string[start: start+len(aim)]:
        chars[ord(char)] += 1

    for char in aim:
        if chars[ord(char)] == 0:
            return False
        chars[ord(char)] -= 1
    return True

# 方法1,复杂度为O(N*M)
def containAim(string, aim):
    if not string or not aim or len(string) < len(aim):
        return -1
    for start in range(len(string)-len(aim)+1):
        if isCountEqual(string, start, aim):
            return start
    return -1

# 方法2：最优解，利用滑动窗口+欠债表，复杂度O(N)
def containAimFinal(string, aim):
    if not string or not aim or len(string) < len(aim):
        return -1
    chars = [0]*256
    for char in aim:
        chars[ord(char)] += 1

    invalid_times = 0
    index = 0
    # 先让窗口拥有len(aim)个字符
    for index in range(len(aim)):
        if chars[ord(string[index])] <= 0:
            invalid_times += 1
        chars[ord(string[index])] -= 1

    for index in range(len(aim), len(string)):
        if invalid_times == 0:
            return index-len(aim)
        # 后面进窗口，进之前为0或负数，多一次无效
        if chars[ord(string[index])] <= 0:
            invalid_times += 1
        chars[ord(string[index])] -= 1

        # 前面出窗口，出窗口之前为负数，减一次无效
        if chars[ord(string[index-len(aim)])] < 0:
            invalid_times -= 1
        chars[ord(string[index-len(aim)])] += 1
    # 对最后一个窗口的判断
    return index - len(aim) if invalid_times == 0 else -1






