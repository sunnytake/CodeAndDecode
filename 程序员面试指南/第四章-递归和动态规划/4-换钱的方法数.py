# coding=utf-8
'''
给定数组arr，arr中所有的值都为正数且不重复。每个值代表一种面值的货币，每种面值的货币
可以使用任意张，再给定一个整数aim代表要找的钱数，求还钱有多少种方法
arr=[5,10,25,1], aim=0
组成0元的方法有1种，就是所有面值的货币都不用，所以返回1
arr=[5,10,25,1], aim=15
组成15元的方法有6种，分别为3张5元、1张10元+1张5元、1张10元+5张1元、
10张1元+1张5元、2张5元+5张1元+、15张1元。所以返回6
arr=[3,5], aim=2
任何方法都无法组成2元，所以返回0
'''

# 暴力递归：时间复杂度非常高，并且与arr中钱的面值有关，最差情况下为O(aim^N)
def coins1(arr, aim):
    if not arr or aim < 0:
        return 0
    return process1(arr, 0, aim)

def process1(arr, index, aim):
    res = 0
    if index == len(arr):
        if aim == 0:
            res = 1
        else:
            res = 0
    else:
        for i in range(aim//arr[index]+1):
            res += process1(arr, index+1, aim - arr[index]*i)
    return res

'''
动态规划方法：
dp[i][j]表示使用arr[0...i]的情况下，组成钱数j的方法

对位置(i,j)来说，dp[i][j]的计算过程需要枚举dp[i-1][0...j]上的所有值，
dp一共有N*aim个位置，所以总体时间复杂度为O(N*aim^2)
'''
def conins(arr, aim):
    if not arr or aim < 0:
        return 0
    dp = []
    # 初始化dp矩阵，第一列初始化为1
    for i in range(len(arr)):
        dp.append([1] + [0]*aim)
    # 第一行初始化
    j = 1
    while arr[0]*j <= aim:
        dp[0][arr[0]*j] = 1
        j += 1

    for i in range(1, len(arr)):
        for j in range(aim+1):
            num = 0
            k = 0
            while j - arr[i]*k >= 0:
                num += dp[i-1][j - arr[i]*k]
                k += 1
            dp[i][j] = num
    return dp[-1][-1]

'''
优化的动态规划：
除第一行和第一列的其它位置，记为位置(i,j)。dp[i][j]的值是以下几个值得累加
* 完全不用arr[i]货币，只使用arr[0...i-1]货币时，方法数为dp[i-1][j]
* 用1张arr[i]货币，剩下的钱用arr[0...i-1]货币组成，方法数为dp[i-1][j-arr[i]]
* 用2张arr[i]货币，剩下的钱用arr[0...i-1]货币组成，方法数为dp[i-1][j-2*arr[i]]
...
* 用k张arr[i]货币，剩下的钱用arr[0...i-1]货币组成，方法数为dp[i-1][j-k*arr[i]]
j - k*arr[i] >= 0, k为非负整数

dp[i-1][j-k*arr[i]]的累加值为dp[i][j-arr[i]]
省去了枚举k的过程，时间复杂度减小至O(N * aim)
'''
def coins(arr, aim):
    if not arr or aim < 0:
        return 0
    dp = []
    for i in range(len(arr)):
        dp.append([1] + [0]*aim)
    # 第一行初始化
    k = 1
    while arr[0]*k <= aim:
        dp[0][arr[0]*k] = 1
        k += 1

    for i in range(1, len(arr)):
        for j in range(1, aim+1):
            dp[i][j] = dp[i-1][j]
            if j - arr[i] >= 0:
                dp[i][j] += dp[i][j-arr[i]]
    return dp[-1][-1]

'''
空间压缩至O(aim)
'''
def coins5(arr, aim):
    if not arr or aim < 0:
        return 0
    dp = [1] + [0]*aim
    k = 1
    while arr[0]*k <= aim:
        dp[arr[0]*k] = 1
        k += 1

    for i in range(1, len(arr)):
        for j in range(1, aim+1):
            if j - arr[i] >= 0:
                dp[j] += dp[j-arr[i]]
    return dp[-1]

















