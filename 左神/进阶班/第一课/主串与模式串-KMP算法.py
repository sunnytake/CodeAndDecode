# coding=utf-8

def KMP(string, pattern):
    '''
    时间复杂度：生成next数组时间复杂度为O(m)，匹配时是对主串的遍历，时间复杂度为O(n)
    链接：https://mp.weixin.qq.com/s/3gYbmAAFh08BQmT-9quItQ
    '''
    if not string or not pattern or len(string) < len(pattern):
        return -1
    l1, l2 = 0, 0
    nexts = getNext(pattern)
    while l1 < len(string) and l2 < len(pattern):
        if string[l1] == pattern[l2]:
            l1 += 1
            l2 += 1
        else:
            if nexts[l2] == -1:
                l1 += 1
            else:
                l2 = nexts[l2]
    return l1-l2 if l2 == len(pattern) else -1


def getNext(pattern):
    if len(pattern) == 1:
        return [-1]
    nexts = [0]*len(pattern)
    nexts[0] = -1
    nexts[1] = 0
    cur = 0
    index = 2
    while index < len(pattern):
        if pattern[index-1] == pattern[cur]:
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
    pattern = "abacab"
    string = "abacaabacabacab"
    string = "abacaabacccabaccab"
    print(KMP(string, pattern))