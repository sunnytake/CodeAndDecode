# coding=utf-8
"""
给你一个数组arr，和一个整数aim
如果可以任意选择arr中的数字，求能不能累加得到aim
注：arr中的数字和aim均为正数

dp[i][j]表示用arr[0...i]是否能湊成整數aim（可以用部分元素）
"""
def reachNum(arr, aim):
    dp = []
    for i in range(len(arr)):
        dp.append([False]*(sum(arr)+1))
    dp[0][arr[0]] = True
    for i in range(1, len(arr)):
        for j in range(sum(arr)):
            if dp[i-1][j]:
                dp[i][j] = True
                dp[i][j+arr[i]] = True
        if dp[i][aim]:
            return True
    return False


def reachNum2(array, aim):
    '''
    暴力递归，借助于求子序列的思想
    '''
    if not array:
        return False
    return process2(array, aim, 0, [])


def process2(array, aim, index, subseq):
    if index == len(array):
        if sum(subseq) == aim:
            return True
        else:
            return False
    return process2(array, aim, index + 1, subseq + [array[index]]) or process2(array, aim, index + 1, subseq)


if __name__ == '__main__':
    arr = [2, 2, 4, 4, 6, 8]
    print(reachNum3(arr, 13))