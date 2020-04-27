# coding=utf-8
"""
给定一个n个整数的数组S，是否存在S中的元素a，b，c，使得a + b + c = target？
查找数组中所有唯一的三元组，它们的总和为target。
"""

def find(array, target):
    if not array or target is None:
        return []
    array = sorted(array)
    for start in range(len(array)-2):
        left, right = start+1, len(array)-1
        while left < right:
            if array[start] + array[left] + array[right] < target:
                left += 1
            elif array[start] + array[left] + array[right] > target:
                right -= 1
            else:
                return [start, left, right]
    return []

class Solution(object):
    def threeSum(self, array):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not array:
            return []
        array = sorted(array)
        res = []
        start = -1
        while start < len(array) - 2:
            start += 1
            if start > 0 and array[start-1] == array[start]:
                continue
            left, right = start + 1, len(array) - 1
            while left < right:
                if array[start] + array[left] + array[right] < 0:
                    left += 1
                elif array[start] + array[left] + array[right] > 0:
                    right -= 1
                else:
                    res.append([array[start], array[left], array[right]])
                    left += 1
                    while left < right and array[left-1] == array[left]:
                        left += 1
        return res

if __name__ == '__main__':
    array = [-1,0,1,0]
    print(Solution().threeSum(array))