# coding=utf-8
'''
大顶推
'''

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def heapSort(array):
    if not array or len(array) < 2:
        return
    for i in range(len(array)):
        heapInsert(array, i)

    heap_size = len(array)-1
    swap(array, 0, heap_size)
    while heap_size > 0:
        heapify(array, 0, heap_size)
        heap_size -= 1
        swap(array, 0, heap_size)

def heapInsert(array, index):
    flag = False
    if index == 10:
        flag = True

    # (0-1)/2在java中为0，(0-1)//2在python中为-1
    while (index-1)//2 >= 0 and array[index] > array[(index-1)//2]:
        swap(array, index, (index-1)//2)
        index = (index-1) // 2

def heapify(array, index, heap_size):
    left = index*2 + 1
    while left < heap_size:
        largest = left + 1 if left+1 < heap_size and array[left+1] > array[left] else left
        largest = largest if array[largest] > array[index] else index
        if largest == index:
            break
        swap(array, largest, index)
        index = largest
        left = index*2 + 1

if __name__ == '__main__':
    array = [1, 3, 5, 7, 2, 4, 6, 5, 3, 5, 10]
    heapSort(array)
    print(array)