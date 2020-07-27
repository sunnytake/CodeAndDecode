# coding=utf-8

def rabinKarp(string, pattern):
    '''
    思想：比较模式串与主串中等长部分的hash值
    时间复杂度：计算单个子串的hash值时间为O(M)，后续的子串hash为增量计算，时间复杂度也为O(N)，总时间复杂度O(M+N)
    缺点：哈希冲突，每次hash冲突都要对模式串和子串逐个字符比较，如果冲突太多，RK算法就退化为暴力算法了
    参考：https://mp.weixin.qq.com/s?__biz=MzIxMjE5MTE1Nw==&mid=2653201142&idx=1&sn=8cac1bbcfdb94474f0cc3855705cc253&chksm=8c99d02cbbee593ae0fb7fa1c8c610e7c1f57009e0c0ecbe19d07f60951912c915bce65c8619&scene=21#wechat_redirect
    '''
    pattern_code = myhash(pattern)
    # 主串中与模式串等长部分的hash值
    str_code = hash(string[len(pattern)])
    for i in range(len(string) - len(pattern) + 1):
        # 仅用hash值碰撞概率，因此hash相同的情况下，进行进一步比较
        if pattern_code == str_code and pattern == string[i: i+len(pattern)]:
            return i
        # 如果不是最后一轮，更新主串的hash值
        if i < len(string) - len(pattern):
            str_code = nextHash(string, i, str_code, len(pattern))
    return -1


def myhash(string):
    '''
    采用按位相加方法来计算hashcode，a当做1,c当做3...
    这样计算hash的方法有较大的碰撞概率，例如abc与bac、cba等
    因此hash相同的情况下，进行进一步比较
    '''
    hashcode = 0
    for char in string:
        hashcode += ord(char) - ord('a')
    return hashcode


def nextHash(string, index, hash, pattern_length):
    hash -= ord(string[index]) - ord('a')
    hash += ord(string[index + pattern_length]) - ord('a')
    return hash