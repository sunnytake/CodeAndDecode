# coding-utf-8
'''
给定 n 个不同的正整数，整数 k（k <= n）以及一个目标数字 target。　
在这 n 个数里面找出 k 个数，使得这 k 个数的和等于目标数字，求问有多少种方案？

输入:
List = [1,2,3,4]
k = 2
target = 5
输出: 2
说明: 1 + 4 = 2 + 3 = 5
样例2

输入:
List = [1,2,3,4,5]
k = 3
target = 6
输出: 1
说明: 只有这一种方案。 1 + 2 + 3 = 6

思想：
    设状态为f[i][j][p]，表示前i个数中找出j个数且和等于p的方案数目
    状态转移方程：f[i][j][p] = f[i-1][j][p] + f[i-1][j-1][p-nums[i]]
'''
def kSum(nums, k, target):
    if not nums or len(nums) < k or k <= 0:
        return 0
    dp = []
    for i in range(len(nums)+1):
        temp = []
        for j in range(k+1):
            temp.append([0] * (target + 1))
        dp.append(temp[:][:])
    for i in range(len(nums)+1):
        dp[i][0][0] = 1
    for i in range(1, len(nums)+1):
        for j in range(1, k+1):
            for t in range(1, target+1):
                dp[i][j][t] = dp[i-1][j][t]
                dp[i][j][t] += dp[i-1][j-1][t - nums[i-1]] if t - nums[i-1] >= 0 else 0
    return dp[len(nums)][k][target]





















