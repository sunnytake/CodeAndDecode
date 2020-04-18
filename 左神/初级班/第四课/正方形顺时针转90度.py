# coding=utf-8

"""
将正方形矩阵旋转90度
例如：
1   2   3
4   5   6
7   8   9
旋转90度后为：
7   4   1
8   5   2
9   6   3
要求：空间复杂度为O(1)
"""

def rotateMatirx(mat):
    left_top, right_down = (0, 0), (len(mat)-1, len(mat[0])-1)
    while left_top[0] < right_down[0]:
        rotateEdge(mat, left_top, right_down)
        left_top = (left_top[0]+1, left_top[1]+1)
        right_down = (right_down[0]-1, right_down[1]-1)

def rotateEdge(mat, left_top, right_down):
    times = right_down[1] - left_top[1]
    for i in range(times):
        temp = mat[left_top[0]][left_top[1]+i]
        mat[left_top[0]][left_top[1]+i] = mat[right_down[0]-i][left_top[1]]
        mat[right_down[0] - i][left_top[1]] = mat[right_down[0]][right_down[1]-i]
        mat[right_down[0]][right_down[1] - i] = mat[left_top[0]+i][right_down[1]]
        mat[left_top[0] + i][right_down[1]] = temp

if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotateMatirx(mat)
    print(mat)

