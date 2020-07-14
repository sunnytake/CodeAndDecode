# coding=utf-8

'''
分治
'''

def mergeSort(array):
    '''
    时间复杂度O(N*logN)
    空间复杂度O(N)
    稳定
    :param array:
    :return:
    '''
    if not array or len(array) < 2:
        return
    process(array, 0, len(array)-1)

def process(array, left, right):
    if left >= right:
        return
    mid = left + ((right-left) >> 1)
    process(array, left, mid)
    process(array, mid+1, right)
    merge(array, left, mid, right)

def merge(array, left, mid, right):
    help = []
    p1, p2 = left, mid+1
    while p1 <= mid and p2 <= right:
        if array[p1] < array[p2]:
            help.append(array[p1])
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
    # 值替换
    array[left:right+1] = help[:]
    return


if __name__ == '__main__':
    array = [3, 1, 8, 10, 2, 9]
    mergeSort(array)
    print(array)
