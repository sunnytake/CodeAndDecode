# coding=utf-8

"""
给定一个整型矩阵matrix，请按照转圈的方式打印它
例如：
1   2   3   4
5   6   7   8
9   10  11  12
12  14  15  16
打印结果为：
1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10
要求：额外空间复杂度为O(1)
"""
def printMatrix(mat):
    if not mat:
        return []
    res = []
    left_top, right_down = (0, 0), (len(mat)-1, len(mat[0])-1)
    while left_top[0] <= right_down[0] and left_top[1] <= right_down[1]:
        printCirclr(mat, left_top, right_down, res)
        left_top = (left_top[0]+1, left_top[1]+1)
        right_down = (right_down[0]-1, right_down[1]-1)
    return res


def printCirclr(mat, left_top, right_down, res):
    if left_top[0] == right_down[0]:
        res += mat[left_top[0]][left_top[1]: right_down[1]+1]
    elif left_top[1] == right_down[1]:
        for row in range(left_top[0], right_down[0]+1):
            res.append(mat[row][left_top[1]])
    else:
        for col in range(left_top[1], right_down[1]):
            res.append(mat[left_top[0]][col])
        for row in range(left_top[0], right_down[0]):
            res.append(mat[row][right_down[1]])
        tmp = []
        for col in range(left_top[1]+1, right_down[1]+1):
            tmp.append(mat[right_down[0]][col])
        res += tmp[::-1]
        tmp = []
        for row in range(left_top[0]+1, right_down[0]+1):
            tmp.append(mat[row][left_top[1]])
        res += tmp[::-1]

if __name__ == '__main__':
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(printMatrix(mat))