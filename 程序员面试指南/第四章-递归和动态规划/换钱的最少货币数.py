# coding=utf-8
'''
给定数组，其中所有值都为正数且不重复。每个值代表一种面值的货币，
每种面值的货币可以使用任意张。给定一个正数代表要找的钱数，求使用的最少货币数
arr=[5,2,3], aim=20
4张5元可以组成20元，其它的找钱方案都要使用更多张货币，所以返回4
arr=[5,2,3], aim=0
不用任何货币就可以组成0元，返回0
arr=[3,5], aim=2
根本无法组成2元，钱不能找开的情况下默认返回-1

如果arr的长度为N，生成行数为N，列数为aim+1的动态规划表dp
dp[i][j]的含义是, 在使用arr[0..i]的情况下，组成j元所需要的最少张数
dp[0...N-1][0]表示aim为0时需要的最少张数，钱数为0时不需要任何货币，设为0即可
dp[0][0...aim]表示只能使用货币arr[0]的情况下，找到某个钱所需要的最小张数
dp[i][j] = min(dp[i-1][j], dp[i][j-arr[j]]+1)
'''
def minCoins1(arr, aim):
    if not arr or aim < 0:
        return -1
    dp = []
    for i in range(len(arr)):
        dp.append([0] + [None]*aim)

    for j in range(1, aim+1):
        if j - arr[0] >= 0 and dp[0][j - arr[0]] is not None:
            dp[0][j] = dp[0][j - arr[0]] + 1

    for i in range(1, len(arr)):
        for j in range(1, aim+1):
            temp_min = None
            if j - arr[i] >= 0 and dp[i][j - arr[i]] is not None:
                temp_min = dp[i][j - arr[i]] + 1
            if temp_min is None or dp[i-1][j] is None:
                dp[i][j] = temp_min if temp_min is not None else dp[i-1][j]
            else:
                dp[i][j] = min(temp_min, dp[i-1][j])
    return dp[-1][-1] if dp[-1][-1] is not None else -1

# 时间复杂度为O(Nxaim)，空间复杂度为O(aim)
def minCoins2(arr, aim):
    if not arr or aim < 0:
        return -1
    dp = [0] + [None]*aim
    for j in range(1, aim+1):
        if j - arr[0] >= 0 and dp[j-arr[0]] is not None:
            dp[j] = dp[j-arr[0]] + 1
    for i in range(len(arr)):
        for j in range(1, aim+1):
            temp_min = None
            if j - arr[i] >= 0 and dp[j - arr[i]] is not None:
                temp_min = dp[j-arr[i]] + 1
            if temp_min is not None and (dp[j] is None or (temp_min < dp[j])):
                dp[j] = temp_min
    return dp[-1] if dp[-1] is not None else -1

'''
扩展题目：
给定数组，其中所有值都为正数且不重复。每个值代表一种面值的货币，
数组中的每个值只能使用一次。aim代表要找的钱数，求组成aim的最少货币数
arr=[5,2,3], aim=20
5元、2元和3元的钱各有一张，所以无法组成20元，默认返回-1
arr=[5,2,5,3], aim=10
5元的货币有2张，可以组成10元，且该方案所需张数最少，返回2
arr=[5,2,5,3], aim=15
所有的钱加起来才能组成15元，返回4
arr = [5,2,5,3], aim=0
不用任何货币就可以组成0元，返回0

dp[i][j]含义：使用aim[0...i]的情况下（每个值仅代表一张货币），组成j所需的最小张数
dp[0...N-1][0]：表示找的钱数为0时需要的最少张数，钱数为0时完全不需要任何货币，设为0即可
'''
def minCoins3(arr, aim):
    if not arr or aim < 0:
        return -1
    dp = []
    for i in range(len(arr)):
        dp.append([0] + [None]*aim)

    if arr[0] <= aim:
        dp[0][arr[0]] = 1

    for i in range(1, len(arr)):
        for j in range(1, aim+1):
            temp_min = None
            # arr[i]只有一张，所以只能使用arr[0...i-1]
            if j - arr[i] >= 0 and dp[i-1][j - arr[i]] is not None:
                temp_min = dp[i-1][j - arr[i]] + 1
            if temp_min is None or dp[i - 1][j] is None:
                dp[i][j] = temp_min if temp_min is not None else dp[i - 1][j]
            else:
                dp[i][j] = min(temp_min, dp[i - 1][j])
    return dp[-1][-1] if dp[-1][-1] is not None else -1

def minCoins4(arr, aim):
    if not arr or aim < 0:
        return -1
    dp = [0] + [None]*aim
    if arr[0] <= aim:
        dp[arr[0]] = 1
    for i in range(1, len(arr)):
        for j in range(1, aim+1):
            temp_min = None
            if j - arr[i] >= 0 and dp[j-arr[i]] is not None:
                temp_min = dp[j-arr[i]] + 1
            if temp_min is not None and (dp[j] is None or (temp_min < dp[j])):
                dp[j] = temp_min
    return dp[-1] if dp[-1] is not None else -1


































