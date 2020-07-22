# coding=utf-8

'''
求将数组中字符串拼接起来后字典序最小的结果
例如：
[ab, cd, ef]
可以拼接为efcdab, abcdef, cdabedm等
最小的为abcdef

贪心：
定一个标准
在一个标准下，快速分出一个先后来

错误：
str1 <= str2, str1放前面，否则str2放前面，如b<=ba, 但是bba>bab
正确：
str+str2 <= str2+str1，str1放前面，否则str2放前面
'''
import functools

def compator(str1, str2):
    # 排在后面的情况，返回正数
    if str1+str2 >= str2+str1:
        return 1
    # 排在前面的情况，返回负数
    else:
        return -1

def lowestString(array):
    if not array:
        return ""
    array.sort(key=functools.cmp_to_key(compator))
    return "".join(array)


if __name__ == '__main__':
    # array = ["ab", "cd", "ef"]
    array = ['b', 'ba']
    print(lowestString(array))

