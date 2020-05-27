# coding=utf-8
'''
给定数组arr，返回arr的最长递增子序列
arr = [2,1,5,3,6,4,8,9,7]，返回的最长递增子序列为[1,3,4,8,9]
'''

# 时间复杂度为O(N^2)
def getdp1(arr):
    dp = [1]*len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp
































