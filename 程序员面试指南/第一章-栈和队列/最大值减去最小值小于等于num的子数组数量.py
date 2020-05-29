# coding=utf-8
'''
给定数组arr和整数num，共返回多少个子数组满足如下情况：
max(arr[i...j]) - min(arr[i...j]) <= num
max(arr[i...j])表示子数组arr[i...j]中的最大值
min(arr[i...j])表示子数组arr[i...j]中的最小值
'''
def getNum(arr, num):
    if not arr:
        return 0
    max_queue, min_queue = [], []
    res = 0
    j = 0
    for i in range(len(arr)):
        while j < len(arr):
            while min_queue and arr[min_queue[-1]] >= arr[j]:
                min_queue.pop(-1)
            min_queue.append(j)
            while max_queue and arr[max_queue[-1]] <= arr[j]:
                max_queue.pop(-1)
            max_queue.append(j)
            if arr[max_queue[0]] - arr[min_queue[0]] > num:
                break
            j += 1
        if min_queue[0] == i:
            min_queue.pop(0)
        if max_queue[0] == i:
            max_queue.pop(0)
        res += j - i
    return res





























