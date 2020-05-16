# coding=utf-8

def getMinKthByBFPRT(array, k):
    return bfprt(array[:], 0, len(array)-1, k-1)

def bfprt(array, begin, end, index):
    if begin == end:
        return array[begin]
    # 以5个为一组进行划分，找到中位数
    pivot = medianOfMedians(array, begin, end)
    # 根据中位数进行划分，返回等于中位数的起始位置和结束位置
    pivot_start, pivot_end = partition(array, begin, end, pivot)
    if index >= pivot_start and index <= pivot_end:
        return array[index]
    elif index < pivot_start:
        return bfprt(array, begin, pivot_start-1, index)
    else:
        return bfprt(array, pivot_end+1, end, index)

def medianOfMedians(array, begin, end):
    num = end - begin + 1
    total_count = num // 5 if num % 5 == 0 else num // 5 + 1
    median_array = []
    count = 0
    index = 0
    while count < total_count:
        count += 1
        start_index = begin + index*5
        end_index = start_index + 4
        median_array.append(get_median(array, start_index, min(end, end_index)))
    return bfprt(median_array, 0, len(median_array)-1, len(median_array)//2)

def get_median(array, start, end):
    insertion_sort(array, start, end)
    sum_val = start + end
    mid = (sum_val // 2) + (sum_val % 2)
    return array[mid]

def insertion_sort(array, begin, end):
    for i in range(begin+1, end+1):
        for j in range(i, begin, -1):
            if array[j-1] > array[j]:
                swap(array, j-1, j)
            else:
                break

def partition(array, begin, end, pivot):
    less, cur, more = begin-1, begin, end+1
    while cur < more:
        if array[cur] < pivot:
            less += 1
            swap(array, less, cur)
            cur += 1
        elif array[cur] > pivot:
            more -= 1
            swap(array, more, cur)
        else:
            cur += 1
    return less+1, more-1

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp