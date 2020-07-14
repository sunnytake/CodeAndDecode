# coding=utf-8

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def cockTailSort(array):
    '''
    第一轮从左到右，第二轮从右到左 ...
    对比冒泡排序，能够在特定条件下（大部分元素已经有序）减少排序的回合数
    '''
    for i in range(len(array) // 2):
        is_sorted = True
        # 奇数轮，从左向右比较和交换
        for j in range(i, len(array)-1-i):
            if array[j] > array[j+1]:
                swap(array, j, j+1)
                is_sorted = False
        if is_sorted:
            break

        is_sorted = True
        # 偶数轮，从右向左比较和交换
        for j in range(len(array)-1-i, i, -1):
            if array[j] < array[j-1]:
                swap(array, j, j-1)
                is_sorted = False
        if is_sorted:
            break
    return

def cockTailSort(array):
    '''
    优化：设置边界值
    '''
    # 从左向右第一次交换的位置
    last_right_exchange_index = 0
    # 从右向左第一次交换的位置
    last_left_exchange_index = 0
    # 无序数列的右边界，每次比较只需要比到这里为止
    right_sort_border = len(array) - 1
    # 无序数列的左边界，每次比较只需要比到这里为止
    left_sort_border = 0
    for i in range(len(array) // 2):
        is_sorted = True
        # 奇数轮，从左向右比较和交换
        for j in range(i, len(array)-1-i):
            if array[j] > array[j+1]:
                swap(array, j, j+1)
                is_sorted = False
                last_right_exchange_index = j
        if is_sorted:
            break

        is_sorted = True
        # 偶数轮，从右向左比较和交换
        for j in range(len(array)-1-i, last, -1):
            if array[j] < array[j-1]:
                swap(array, j, j-1)
                is_sorted = False
                last_left_exchange_index = j
        if is_sorted:
            break
    return

if __name__ == '__main__':
    array = [3, 1, 8, 10, 2, 9]
    cockTailSort(array)
    print(array)