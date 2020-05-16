# coding=utf-8

"""
小和问题：
在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组的小和
例如：[1, 3, 4, 2, 5]
1左边比1小的数，没有
3左边比3小的数，1
4左边比4小的数：1, 3
2左边比2小的数：1
5左边比5小的数：1， 3， 4， 2
所以小和为1+1+3+1+1+3+4+2=16

逆序对问题：
在一个数组中，左边的数如果比右边的数大，则这两个数构成一个逆序对，请打印所有逆序
"""
'''
分治
'''

def minSum(array):
    if not array or len(array) < 2:
        return 0
    return minSumProcess(array, 0, len(array)-1)

def minSumProcess(array, left, right):
    if left == right:
        return 0
    mid = left + ((right - left) // 2)
    return minSumProcess(array, left, mid) + minSumProcess(array, mid+1, right) + merge(array, left, mid, right)

def merge(array, left, mid, right):
    help = []
    min_sum = 0
    p1, p2 = left, mid+1
    while p1 <= mid and p2 <= right:
        if array[p1] < array[p2]:
            help.append(array[p1])
            min_sum += array[p1]*(right-p2+1)
            p1 += 1
        else:
            help.append(array[p2])
            p2 += 1
    while p1 <= mid:
        help.append(array[p1])
        p1 += 1
    while p2 <= right:
        help.append(array[p2])
        p2 += 1
    array[left: right+1] = help[:]
    return min_sum

if __name__ == '__main__':
    array = [1, 3, 4, 2, 5]
    print(minSum(array))