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
    '''
    小和问题
    '''
    if not array or len(array) < 2:
        return 0
    return minSumProcess(array, 0, len(array)-1)

def minSumProcess(array, left, right):
    if left == right:
        return 0
    mid = left + ((right - left) // 2)
    return minSumProcess(array, left, mid) + minSumProcess(array, mid+1, right) + minSumMerge(array, left, mid, right)

def minSumMerge(array, left, mid, right):
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


def reverseTuple(array):
    '''
    逆序对问题
    '''
    if not array or len(array) < 2:
        return []

    return reverseTupleProcess(array, 0, len(array)-1)


def reverseTupleProcess(array, left, right):
    if left >= right:
        return []
    res = []
    mid = (left + right) // 2
    res += reverseTupleProcess(array, left, mid)
    res += reverseTupleProcess(array, mid+1, right)
    res += reverseTupleMerge(array, left, mid, right)
    return res


def reverseTupleMerge(array, left, mid, right):
    res = []
    p1, p2 = left, mid + 1
    help_array = []
    while p1 <= mid and p2 <= right:
        if array[p1] <= array[p2]:
            help_array.append(array[p1])
            for val in array[mid+1: p2]:
                res.append((array[p1], val))
            p1 += 1
        else:
            help_array.append(array[p2])
            p2 += 1
    while p1 <= mid:
        help_array.append(array[p1])
        for val in array[mid+1: p2]:
            res.append((array[p1], val))
        p1 += 1
    while p2 <= right:
        help_array.append(array[p2])
        p2 += 1
    array[left: right+1] = help_array[:]
    return res

if __name__ == '__main__':
    array = [1, 3, 4, 2, 5]
    print(minSum(array))
    array = [1, 3, 4, 2, 5]
    print(reverseTuple(array))