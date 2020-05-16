# coding=utf-8

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def bubbleSort(array):
    '''
    相邻元素不断交换位置
    '''
    if not array or len(array) < 2:
        return
    for end in range(len(array)-1, 0, -1):
        for i in range(0, end, 1):
            if array[i] > array[i+1]:
                swap(array, i, i+1)
    return

if __name__ == '__main__':
    array = [3, 1, 8, 10, 2, 9]
    bubbleSort(array)
    print(array)