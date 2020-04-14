# coding=utf-8

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def quickSort(array):
    if not array or len(array) < 2:
        return
    startSort(array, 0, len(array)-1)
    return

def startSort(array, start, end):
    if start >= end:
        return
    while start < end:
        mid = start + (end - start) >> 1
        while array[start] <= array[mid] and start < end:
            start += 1
        while array[end] > array[mid] and start < end:
            end -= 1
        if start < end:
            swap(array, start, end)
    return



if __name__ == '__main__':
    array = [3, 1, 8, 10, 2, 9]
    quickSort(array)
    print(array)