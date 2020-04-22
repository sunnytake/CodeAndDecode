# coding=utf-8
"""
给你一个数组arr，和一个整数aim
如果可以任意选择arr中的数字，求能不能累加得到aim
注：arr中的数字和aim均为正数
"""
def dp(arr, aim):
    res_mat = []
    for i in range(len(arr)):
        res_mat.append([False]*(sum(arr)+1))
    res_mat[0][arr[0]] = True
    for i in range(1, len(arr)):
        for j in range(sum(arr)):
            if res_mat[i-1][j]:
                res_mat[i][j] = True
                res_mat[i][j+arr[i]] = True
        if res_mat[i][aim]:
            return True
    return False

def recur(arr, aim):
    '''
    暴力递归
    :param arr:
    :param aim:
    :return:
    '''
    def process(arr, index, temp_sum, aim):
        if index == len(arr):
            return temp_sum == aim
        return process(arr, index+1, temp_sum, aim) or process(arr, index+1, temp_sum+arr[index], aim)
    return process(arr, 0, 0, aim)


if __name__ == '__main__':
    arr = [2, 2, 4, 4, 6, 8]
    print(dp(arr, 18))