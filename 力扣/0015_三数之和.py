# coding=utf-8
'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

思想：
1. 特判：对于数组长度n，如果数组为null或者数组长度小于3，返回[]
2. 对数组进行排序
3. 遍历排序后的数组
    * 若nums[i] > 0：因为已经排序好，所以后面不可能有三个数相加等于0，直接返回结果
    * 对于重复元素：跳过，避免出现重复解
    * 令左指针left=i+1，右指针right=length-1，当left<right时，执行循环：
        * 当nums[i]+nums[left]+nums[right]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。
          并同时将left，right移到下一个位置，寻找新的解
        * 若和大于0，说明nums[right]太大，right左移
        * 若和小于0，说明nums[left]太小，left右移
'''
def threeSum(nums):
    length = len(nums)
    if not nums or length < 3:
        return []
    nums.sort()
    res = []
    for i in range(length):
        if nums[i] > 0:
            return res
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i + 1, length - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] == 0:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif nums[i] + nums[left] + nums[right] > 0:
                right -= 1
            else:
                left += 1
    return res

























