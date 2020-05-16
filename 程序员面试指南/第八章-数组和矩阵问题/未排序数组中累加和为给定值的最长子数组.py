# coding=utf-8
'''
给定一个无序数组arr，其中元素可正、可负、可0，给定一个整数k，
求arr所有的子数组中累加和为k的最长子数组长度
'''
# 时间复杂度O(N)，空间复杂度O(N)
def getMaxLength(array, k):
    if not array or k <= 0:
        return 0
    # key为array[0]到array[i]的累加和，value为当前值的下标
    sum_index = {0: -1}
    sum_val = 0
    max_len = 0
    for index, val in enumerate(array):
        sum_val += val
        if (sum_val - k) in sum_index:
               max_len = max(index-sum_index[sum_val-k], max_len)
        # sum_index只用记录sum_val出现的最早位置即可，因为是最长子数组
        if sum_val not in sum_index:
            sum_index[sum_val] = index
    return max_len

'''
给定一个无序数组arr，其中元素可正、可负、可0，给定一个整数k，
求arr所有的子数组中正数与负数个数相等的最长子数组长度
'''
# 将正数全部变为1，负数全部变为-1，0不变，然后求累加和为0的最长子数组长度即可

'''
给定一个无序数组arr，其中元素只是1或0，
求arr所有的子数组中0和1个数相等的最长子数组长度
'''
# 把数组中的0全部变成-1，1不变，然后求累加和为0的最长子数组长度即可