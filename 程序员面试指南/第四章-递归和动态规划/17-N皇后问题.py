# coding=utf-8
'''
在NxN的棋盘上要摆N个皇后，要求任意两个皇后不同行、不同列、也不在同一条斜线上。
给定一个整数n，返回n皇后的摆法有多少种

n=1， 返回1
n=2/3，无论如何摆都不行，返回0
n=8，返回92

如果在(i, j)位置（第i行第j列）放置了一个皇后，接下来哪些位置不能放皇后？
1. 整个第i行的位置都不能放置
2. 整个第j列的位置都不能放置
3. 如果位置(a, b)满足|a-i| == |b-j|，说明(a,b)与(i,j)在同一条斜线上，也不能放置

把递归过程设计为逐行放置皇后的方式，可以避开条件1的那些不能放置的位置
record数组保存已放置的皇后位置,record[i]表示第i行皇后所在的列数
'''
def num1(n):
    if n < 1:
        return 0
    record = [None]*n
    return process1(record, 0, n)

def process1(record, index, n):
    if index == n:
        return 1
    res = 0
    for j in range(n):
        if isValid(record, index, j):
            record[index] = j
            res += process1(record, index+1, n)
    return res

def isValid(record, i, j):
    for k in range(i):
        if j == record[k] or abs(i-k) == abs(j - record[k]):
            return False
    return True























