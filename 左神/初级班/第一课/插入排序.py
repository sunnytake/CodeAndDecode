# coding=utf-8

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def insertSort(array):
    '''
    冒泡排序：每次在无序部分找到一个最大的或者最小的，放在有序部分的末尾
    插入排序：每次从无序部分取一个元素插入到有序部分，插入排序也是稳定的
    '''
    if not array or len(array) < 2:
        return
    # 第0个元素已经有序，从第1个开始插入
    for i in range(1, len(array)):
        # 和要插入元素前面的有序部分进行比较
        for j in range(i-1, -1, -1):
            if array[j] > array[j+1]:
                swap(array, j, j+1)
    return

if __name__ == '__main__':
    array = [3, 1, 8, 10, 2, 9]
    insertSort(array)
    print(array)