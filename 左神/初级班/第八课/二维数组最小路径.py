# coding=utf-8

"""
给一个二维数组，二维数组中的每个数都是正数
要求从左上角走到右下角，每一步只能向右或者向下
沿途经过的数字累加起来，求最小的路径和
"""

def walk1(mat):
    '''
    动态规划
    '''
    res_mat = []
    for i in range(len(mat)):
        res_mat.append([0]*len(mat[0]))
    res_mat[0][0] = mat[0][0]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                res_mat[i][j] = mat[i][j] + res_mat[i][j-1]
            elif j == 0:
                res_mat[i][j] = mat[i][j] + res_mat[i-1][j]
            else:
                res_mat[i][j] = mat[i][j] + min(res_mat[i][j-1], res_mat[i-1][j])
    return res_mat[len(mat)-1][len(mat[0])-1]



def walk(mat, i, j):
    '''
    暴力递归
    从(i,j)出发到右下角的最小路径和
    '''
    if i == len(mat)-1 and j == len(mat[0])-1:
        return mat[i][j]
    if i == len(mat)-1:
        return mat[i][j] + walk(mat, i, j+1)
    if j == len(mat[0]) - 1:
        return mat[i][j] + walk(mat, i+1, j)
    # 走右边到右下角的最短路径和
    right_path= walk(mat, i, j+1)
    # 走下边到右下角的最短路径和
    down_path = walk(mat, i+1, j)
    return mat[i][j] + min(right_path, down_path)

if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(walk1(mat))