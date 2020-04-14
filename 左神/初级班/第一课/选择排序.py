# coding=utf-8

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def selectionSort(array):
    if not array or len(array) < 2:
        return
    for i in range(0, len(array)-1, 1):
        min_index = i
        for j in range(i+1, len(array), 1):
            min_index = j if array[j] < array[min_index] else min_index
        swap(array, i, min_index)
    return

if __name__ == '__main__':
    array = [3, 1, 8, 10, 2, 9]
    selectionSort(array)
    print(array)
