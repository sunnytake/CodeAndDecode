# coding=utf-8
import random

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def quickSort(array):
    if not array or len(array) < 2:
        return
    process(array, 0, len(array)-1)

def process(array, left, right):
    if left < right:
        swap(array, left + int(random.random()*(right-left+1)), right)
        com_left, com_right = partition(array, left, right)
        process(array, left, com_left-1)
        process(array, com_right+1, right)

def partition(array, left, right):
    # array[right]作为划分值
    less, more, cur = left-1, right, left
    while cur < more:
        if array[cur] < array[right]:
            less += 1
            swap(array, cur, less)
            cur += 1
        elif array[cur] > array[right]:
            more -= 1
            swap(array, cur, more)
        else:
            cur += 1
    # 交换array[right]和array[more]的值，因为array[more]一定大于array[right]
    swap(array, more, right)
    return less+1, more

if __name__ == '__main__':
    array = [1, 3, 5, 7, 2, 4, 6, 5, 3, 5, 10]
    quickSort(array)
    print(array)