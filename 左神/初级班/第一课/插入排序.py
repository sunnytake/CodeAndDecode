# coding=utf-8

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def insertSort(array):
    if not array or len(array) < 2:
        return
    for i in range(1, len(array), 1):
        for j in range(i-1, -1, -1):
            if array[j] > array[j+1]:
                swap(array, j, j+1)
    return

if __name__ == '__main__':
    array = [3, 1, 8, 10, 2, 9]
    insertSort(array)
    print(array)