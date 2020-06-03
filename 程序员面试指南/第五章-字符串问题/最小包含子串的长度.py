# coding=utf-8
'''
给定字符串str1和str2，求str1的子串中含有str2所有字符的最小子串长度

    str1="abcde", str2="ac"。因为"abc"包含str2的所有字符，并且在满足这一条件的str1
的所有子串中，"abc"是最短的，返回3
    str1="12345"，str2="344"。最小包含子串不存在，返回0
'''
def minLength(str1, str2):
    if not str1 or not str2 or len(str1) < len(str2):
        return 0
    map = [0] * 256
    for char in str2:
        map[char] += 1
    left, right = 0, 0
    match = len(str2)
    min_len = len(str1)+1

    while right != len(str1):
        map[str1[right]] -= 1
        if map[str1[right]] >= 0:
            match -= 1
        if match == 0:
            while map[str1[left]] < 0:
                map[str1[left]] += 1
                left += 1
            min_len = min(min_len, right-left+1)
            match += 1
            map[str1[left]] += 1
            left += 1
        right += 1
    if min_len == len(str1) + 1:
        return 0
    return min_len
























