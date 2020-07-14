# coding=utf-8
'''
快速排序、归并排序、堆排序的差异
性能：
    快速排序平均时间复杂度O(N*logN)，最坏时间复杂度为O(N^2)
    归并排序和堆排序的时间复杂度稳定在O(N*logN)
    平均时间复杂度虽然都是O(N*logN)，但是堆排序性能相对略低，因为二叉堆的父子节点在内存中并不连续
稳定性：
    归并排序是稳定排序
    快速排序和堆排序是不稳定排序
快速排序和堆排序是原地排序，不需要开辟额外空间。而归并排序是非原地排序，merge时需要借助额外的辅助数组
参考博客：https://blog.csdn.net/armlinuxww/article/details/105005320
'''

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def heapSort(array):
    '''
    大顶推
    时间复杂度为O(N*logN)，空间复杂度为O(1)
    堆排序和快速排序的时间复杂度都是O(N*logN)，并且都是不稳定排序
    快速排序的最坏时间复杂度为O(N^2)，而堆排序最坏时间复杂度稳定在O(N*logN)
    '''
    if not array or len(array) < 2:
        return
    # 堆排序的步骤：
    # 1.把无序数组构建成二叉堆
    for index in range(len(array)):
        heapInsert(array, index)

    # 2.循环删除堆顶元素，移到集合尾部，调节堆产生新的堆顶
    heap_size = len(array)-1
    swap(array, 0, heap_size)
    while heap_size > 0:
        heapify(array, 0, heap_size)
        heap_size -= 1
        swap(array, 0, heap_size)

def heapInsert(array, index):
    '''
    初始化数组，使其满足大顶堆的特征，即：从下到上，父节点大于两个子节点
    正是因为这样的初始化，才使得heapify时的调整如此简单
    但是此时问题在于：左右子节点大小不确定
    '''
    # (0-1)/2在java中为0，(0-1)//2在python中为-1
    while (index-1)//2 >= 0 and array[index] > array[(index-1)//2]:
        swap(array, index, (index-1)//2)
        index = (index-1) // 2

def heapify(array, index, heap_size):
    '''
    可以看做此时新增元素放在了index位置（一直为0）
    需要从顶向下调整，堆大小为[0, heap_size)
    '''
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