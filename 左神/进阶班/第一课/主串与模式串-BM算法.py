# coding=utf-8

def boyerMoore(string, pattern):
    '''
    阉割版BM算法，只用了坏字符规则
    链接：https://mp.weixin.qq.com/s?__biz=MzIxMjE5MTE1Nw==&mid=2653201540&idx=1&sn=645a3f5f3fbf30be4f6d1c23eebdf0e7&chksm=8c99d65ebbee5f482dd68efecf7b2a23e98b238ba04c1d3a6aed6c12cab76d4650c3bef5ea00&scene=21#wechat_redirect
    :param string:
    :param pattern:
    :return:
    '''
    # 主串中比较的起始位置
    start = 0
    while start <= len(string) - len(pattern):
        flag = True
        # 从后向前，逐个字符比较
        for i in range(len(pattern)-1, -1, -1):
            if string[start + i] != pattern[i]:
                # 记录坏字符在模式串中的位置
                flag = i
                # 发现坏字符，跳出比较，i记录了坏字符的位置
                break
        if flag is True:
            # 匹配成功，返回主串开始的位置
            return start
        # 寻找坏字符在模式串的对应
        char_index = findCharacter(pattern, string[start + flag], flag)
        # 计算坏字符产生的位移
        offset = flag - char_index if char_index >= 0 else flag + 1
        start += offset
    return -1


def findCharacter(pattern, bad_char, index):
    for i in range(index-1, -1, -1):
        if pattern[i] == bad_char:
            return i
    # 模式串不存在该字符，返回-1
    return -1
