# coding=utf-8
'''
给定一个数组arr,该数组无序，但每个值均为正数，再给定一个正数k。
求arr的所有子数组中所有元素相加和为k的最长子数组长度
例如,arr=[1,2,1,1,1], k=3
累加和为3的最长子数组为[1,1,1]，所以结果返回为3
'''
# 时间复杂度为O(N)，空间复杂度为O(N)
def getMaxLength(array, k):
    if not array:
        return 0
    left, right = 0, 0
    sum_val = array[0]
    max_len = 0
    while right < len(array):
        if sum_val == k:
            max_len = max(right-left+1, max_len)
            sum_val -= array[left]
            left += 1
        elif sum_val < k:
            right += 1
            sum_val += array[right]
        else:
            sum_val -= array[left]
            left -= 1
    return max_len