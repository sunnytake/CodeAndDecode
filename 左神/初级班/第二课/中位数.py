# coding=utf-8

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def midNum(array):
    '''
    有数先放入big_heap中，然后把最大的弹出到min_heap中
    '''
    if not array:
        return None
    big_heap, min_heap = [], []
    for val in array:
        big_heap.append(val)
        bigHeapAdjust(big_heap)
        if len(big_heap) - len(min_heap) > 1:
            num = big_heap.pop(0)
            min_heap.append(num)
            minHeapAdjust(min_heap)

    if len(big_heap) > len(min_heap):
        return big_heap[0]
    else:
        return (big_heap[0] + min_heap[0]) / 2


def midNum(array):
    '''
    有数先放入min_heap中，然后把最小的弹出到big_heap中
    '''
    if not array:
        return None
    big_heap, min_heap = [], []
    for val in array:
        min_heap.append(val)
        minHeapAdjust(min_heap)
        if len(min_heap) - len(big_heap) > 1:
            num = min_heap.pop(0)
            big_heap.append(num)
            bigHeapAdjust(big_heap)

    if len(min_heap) > len(big_heap):
        return min_heap[0]
    else:
        return (big_heap[0] + min_heap[0]) / 2


# 同heapInsert，只不过插入的位置固定位最后一位
def bigHeapAdjust(heap):
    index = len(heap)-1
    while (index-1)//2 >= 0 and heap[index] > heap[(index-1)//2]:
        swap(heap, index, (index-1)//2)
        index = (index-1) // 2

def minHeapAdjust(heap):
    index = len(heap)-1
    while (index - 1) // 2 >= 0 and heap[index] < heap[(index - 1) // 2]:
        swap(heap, index, (index - 1) // 2)
        index = (index - 1) // 2

if __name__ == '__main__':
    array = [1, 3, 7, 2, 4, 6, 3, 10]
    print(sorted(array))
    print(midNum(array))