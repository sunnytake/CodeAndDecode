# coding=utf-8

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def mergeSort(array):
    if not array or len(array) < 2:
        return
    sortProcess(array, 0, len(array)-1)

def sortProcess(array, left, right):
    if left >= right:
        return
    mid = left + ((right-left) >> 1)
    sortProcess(array, left, mid)
    sortProcess(array, mid+1, right)
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


if __name__ == '__main__':
    array = [3, 1, 8, 10, 2, 9]
    mergeSort(array)
    print(array)
