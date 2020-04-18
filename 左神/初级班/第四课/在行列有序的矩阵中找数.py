# coding=utf-8

"""
在行列都排好序的矩阵中找数：
给定一个有N*M的整型矩阵matrix和一个整数K，
matrix的每一行和每一列都是排好序的。实现一个函数，判断K
是否在matrix中。例如：
0   1   2   5
2   3   4   7
4   4   4   8
5   7   7   9
如果K为7，返回true；如果k为6，返回false
要求时间复杂度为O（N+M），额外空间复杂度为O(1)
"""

def findInMatrix(mat, num):
    row, col = 0, len(mat[0])-1
    while row < len(mat) and col >= 0:
        if mat[row][col] < num:
            row += 1
        elif mat[row][col] > num:
            col -= 1
        else:
            return True
    return False

if __name__ == '__main__':
    mat = [[0, 1, 2, 5], [2, 3, 4, 7], [4, 4, 4, 8], [5, 7, 7, 9]]
    num = 6
    print(findInMatrix(mat, num))