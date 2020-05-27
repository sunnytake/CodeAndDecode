# coding=utf-8
'''
给定一个矩阵，从左上角开始每次只能向右或者向下走，最后到达右下角的位置，
路径上所有的数字累加起来就是路径和，返回所有的路径中最小的路径和。

例如：
1   3   5   9
8   1   3   4
5   0   6   1
8   8   4   0
路径1,3,1,0,6,1,0是所有路径中路径和最小的，所以返回12

dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + mat[i][j]
'''

# 时间复杂度O(MxN)，空间复杂度为O(MxN)
def minPathSum1(mat):
    if not mat or not mat[0]:
        return 0

    dp = []
    for i in range(len(mat)):
        dp.append([0]*len(mat[0]))

    # 第一列
    dp[0][0] = mat[0][0]
    for row in range(1, len(mat)):
        dp[row][0] = dp[row-1][0] + mat[row][0]
    # 第一行
    for col in range(1, len(mat[0])):
        dp[0][col] = dp[0][col-1] + mat[0][col]

    for row in range(1, len(mat)):
        for col in range(1, len(mat[0])):
            dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + mat[row][col]
    return dp[-1][-1]

# 时间复杂度为O(MxN)，空间复杂度为O(min(M, N))
def minPathSum2(mat):
    if not mat or not mat[0]:
        return 0
    # 行数与列数较大的为more
    more = max(len(mat), len(mat[0]))
    # 行数与列数较小的为less
    less = min(len(mat), len(mat[0]))
    # 行数是否大于列数
    rowmore = more == len(mat)
    dp = [0] * less
    dp[0] = mat[0][0]
    for i in range(1, less):
        if rowmore:
            dp[i] = dp[i-1] + mat[0][i]
        else:
            dp [i] = dp[i-1] + mat[i][0]

    for i in range(1, more):
        if rowmore:
            dp[0] += mat[i][0]
        else:
            dp[0] += mat[0][i]
        for j in range(1, less):
            # 从左(此时dp[j-1]已经更新过)，从上
            dp[j] = min(dp[j-1], dp[j])
            if rowmore:
                dp[j] += mat[i][j]
            else:
                dp[j] += mat[j][i]
    return dp[-1]
































