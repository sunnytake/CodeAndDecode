# coding=utf-8
"""
一个矩阵中只有0和1两种值，每个位置都可以和自己的上、下、左、右四个位置相连，
如果有一片1连在一起，这个部分叫做一个岛，求一个矩阵中有多少个岛。
例如：
0   0   1   0   1   0
1   1   1   0   1   0
1   0   0   1   0   0
0   0   0   0   0   0
这个矩阵中有3个岛
"""
def coutIsLand(mat):
    if mat is None or mat[0] is None:
        return 0
    count = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                count += 1
                infect(mat, i, j)
    return count

def infect(mat, i, j):
    if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]) or mat[i][j] != 1:
        return
    mat[i][j] = 2
    infect(mat, i+1, j)
    infect(mat, i-1, j)
    infect(mat, i, j+1)
    infect(mat, i, j-1)

if __name__ == '__main__':
    mat = [[0,0,1,0,1,0], [1,1,1,0,1,0], [1,0,0,1,0,0], [0,0,0,0,0,0]]
    print(coutIsLand(mat))