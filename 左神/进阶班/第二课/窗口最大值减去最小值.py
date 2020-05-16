# coding=utf-8

"""
最大值减去最小值小于等于num的子数组数量：
给定数组array和整数num，返回共有多少个子数组满足如下情况：
max(array[i ... j]) - min(array[i ... j]) <= num
max(array[i ... j])表示子数组array[i ... j]中的最大值
min(array[i ... j])表示子数组array[i ... j]中的最小值
"""
def getNum(array, num):
    if not array:
        return 0
    min_array, max_array = [], []
    start, end, res = 0, 0, 0
    while start < len(array):
        while end < len(array):
            while min_array and array[min_array[0]] >= array[end]:
                min_array.pop(0)
            min_array.append(end)
            while max_array and array[max_array] <= array[end]:
                max_array.pop(0)
            max_array.append(end)
            if array[max_array[0]] - array[min_array[0]] > num:
                break
            end += 1
        if min_array[0] == start:
            min_array.pop(0)
        if max_array[0] == start:
            max_array.pop(0)
        res += end - start
        start += 1
    return res