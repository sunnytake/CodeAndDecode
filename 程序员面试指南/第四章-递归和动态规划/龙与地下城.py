# coding=utf-8
'''
给定一个二维数组map，含义是一张地图，例如，如下矩阵
-2      -3      3
-5      -10     1
0       30      -5
游戏规则如下：
* 骑士从左上角出发，每次只能向右或者向下走，最后到达右下角见到公主
* 地图中每个位置的值代表骑士要遭遇的事情。如果是负数，说明此处有怪兽，
要让骑士损失血量。如果是非负数，代表此处有血瓶，能让骑士回血。
* 骑士从左上角到右下角的过程中，走到任何一个位置时，血量都不能少于1
为了保证骑士能见到公主，初始血量至少是多少？根据map，返回初始血量

dp[i][j]：骑士要走上位置(i, j)，并且从该位置选一条最优的路径，最后走到右下角，
骑士起码应该具备的血量
'''
def minHp1(mat):
    if not mat or not mat[0]:
        return 1
    dp = []
    for i in range(len(mat)):
        dp = [None]*len(mat[0])
    dp[-1][-1] = 1 if mat[-1][-1] > 0 else -mat[-1][-1]+1

    # 行初始化
    for j in range(len(mat)-1, -1, -1):
        dp[len(mat)-1][j] = max(dp[len(mat)-1][j+1]-mat[len(mat)-1][j], 1)
    # 列初始化
    for i in range(len(mat)-1, -1, -1):
        dp[i][len(mat[0]) - 1] = max(1, dp[i + 1][len(mat[0]) - 1] - mat[i][len(mat[0]) - 1])

    for i in range(len(mat)-1, -1, -1):
        for j in range(len(mat[0])-1, -1, -1):
            right = max(dp[i][j+1]-mat[i][j], 1)
            down = max(dp[i+1][j] - mat[i][j], 1)
            dp[i][j] = min(right, down)
    return dp[0][0]































