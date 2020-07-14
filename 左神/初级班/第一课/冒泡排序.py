# coding=utf-8

'''
算法比较：冒泡排序、插入排序、选择排序
性能：
    冒泡排序和插入排序的元素比较次数取决于原始数组的有序程度
    选择排序的元素比较次数是固定的，和原始数组的有序程度无关
    当原始数组接近有序时，插入排序性能最优；当原始数组大部分元素无序时，选择排序性能最优
稳定性：
    冒泡排序、插入排序是稳定排序
    选择排序是不稳定排序（https://mp.weixin.qq.com/s?__biz=MzIxMjE5MTE1Nw==&mid=2653198991&idx=1&sn=7f98d59898a911e1425baa6cc180c598&chksm=8c99e855bbee61439086680ceefef33c56038c5d552ae64c1d6135abe467b617aa62f4934f36&scene=21#wechat_redirect）
'''

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def bubbleSort(array):
    '''
    相邻元素两两比较，根据大小来交换元素的位置
    每一轮把一个最小的元素移动到最左侧/把一个最大的元素移动到最右侧
    具有稳定性
    '''
    if not array or len(array) < 2:
        return
    for i in range(len(array)-1):
        # 标志位：数组是否已经有序
        is_sorted = True
        for j in range(0, len(array)-1-i):
            if array[j] > array[j+1]:
                swap(array, j, j+1)
                is_sorted = False
        if is_sorted:
            break
    return

def bubbleSort(array):
    '''
    问题：数组的有序区长度可能大于排序次数，因此后面很多次元素比较是没有意义的
    解决方法：在每一轮排序的最后，记录下最后一次元素交换的位置
    '''
    if not array or len(array) < 2:
        return
    # 记录最后一次交换的位置：即为无序数列的边界
    lastExchangeIndex = len(array)-1
    # 无序数组的边界，每次只需要比到这里为止
    sort_border = len(array) - 1
    for i in range(len(array)-1):
        # 标志位：数组是否已经有序
        is_sorted = True
        for j in range(sort_border):
            if array[j] > array[j+1]:
                swap(array, i, i+1)
                is_sorted = False
                lastExchangeIndex = j
        if is_sorted:
            break
        sort_border = lastExchangeIndex
    return

if __name__ == '__main__':
    array = [3, 1, 8, 10, 2, 9]
    bubbleSort(array)
    print(array)