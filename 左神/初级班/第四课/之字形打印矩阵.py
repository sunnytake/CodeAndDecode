# coding=utf-8

"""
之字形打印矩阵
例如：
1   2   3   4
5   6   7   8
9   10  11  12
之字形打印为：
1
2   5
9   6   3
4   7   10
11  8
12
可以自己在本子上画一下
"""

def printMatZigzag(mat):
    res = []
    from_up = False
    right_top, left_down = (0, 0), (0, 0)
    while right_top[0] < len(mat) and right_top[1] < len(mat[0]):
        res += printEdge(mat, right_top, left_down, from_up)
        from_up = not from_up
        right_top = (right_top[0]+1 if right_top[1] + 1 == len(mat[0]) else right_top[0], right_top[1]+1 if right_top[1] + 1 < len(mat[0]) else right_top[1])
        left_down = (left_down[0]+1 if left_down[0] + 1 < len(mat) else left_down[0], left_down[1]+1 if left_down[0]+1 == len(mat) else left_down[1])
    return res


def printEdge(mat, right_top, left_down, flag):
    res = []

    while right_top[0] <= left_down[0]:
        print(right_top, left_down)
        res.append(mat[right_top[0]][right_top[1]])
        right_top = (right_top[0]+1, right_top[1]-1)

    if flag:
        return res
    else:
        return res[::-1]

if __name__ == '__main__':
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(printMatZigzag(mat))