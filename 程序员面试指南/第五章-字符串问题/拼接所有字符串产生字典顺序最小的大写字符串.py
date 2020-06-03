# coding=utf-8
'''
给定一个字符串类型的数组strs，请找到一种拼接顺序，使得将所有的字符串拼接起来
组成的大写字符串是所有可能性中字典顺序最小的，并返回这个大写字符串

strs=["abc", "de"]，可以拼接成"abcde"，也可以拼成"deabc"，但前面的字典顺序更小，所以返回"abcde"
strs=["b","ba"]，可以拼成"bba"，也可以拼成"bab"，但后者的字典顺序更小，所以返回"bab"
'''

def compator(str1, str2):
    max_length = max(len(str1), len(str2))
    if len(str1) < max_length:
        str1 += str1[-1] * (max_length - len(str1))
    if len(str2) < max_length:
        str2 += str2[-1] * (max_length - len(str2))
    if str1 >= str2:
        return 1
    else:
        return -1

def lowerString(strs):
    import functools
    strs = sorted(strs, key=functools.cmp_to_key(compator))
    return "".join(strs)

if __name__ == '__main__':
    strs = ["b", "ba"]
    print(lowerString(strs))