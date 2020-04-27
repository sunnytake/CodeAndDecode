# coding=utf-8
"""
快速找出一个数组中的两个数字，让这两个数字之和等于一个给定的值。
"""

def find(array, target):
    if not array or target is None:
        return []
    array = sorted(array)
    left, right = 0, len(array)-1
    while left < right:
        if array[left] + array[right] < target:
            left += 1
        elif array[left] + array[right] > target:
            right -= 1
        else:
            return [array[left], array[right]]
    return []