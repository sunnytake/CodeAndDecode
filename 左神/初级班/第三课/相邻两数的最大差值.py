# coding=utf-8

"""
给定一个数组，求如果排序之后，相邻两数的最大差值，
要求时间复杂度为O(N)，且要求不能用非基于比较的排序
"""

def getBucketId(val, length, min_val, max_val):
    return ((val - min_val) * length) // (max_val - min_val)


def maxDiff(array):
    if not array or len(array) < 2:
        return 0
    min_val, max_val = min(array), max(array)
    # 第一位：桶中是否有数据，第二位：桶中最小值，第三位：桶中最大值
    buckets = [(False, None, None) for i in range(len(array) + 1)]
    for val in array:
        bucket_id = getBucketId(val, len(array), min_val, max_val)
        if not buckets[bucket_id][0]:
            buckets[bucket_id] = [True, val, val]
        else:
            buckets[bucket_id][1] = val if val < buckets[bucket_id][1] else buckets[bucket_id][1]
            buckets[bucket_id][2] = val if val > buckets[bucket_id][2] else buckets[bucket_id][2]

    res = 0
    last_max = buckets[0][2]
    for bucket in buckets[1:]:
        if bucket[0]:
            res = max(res, bucket[1]-last_max)
            last_max = bucket[2]
    return res

if __name__ == '__main__':
    array = [1, 3, 8, 13, 5, -1]
    print(maxDiff(array))


