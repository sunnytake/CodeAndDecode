# coding=utf-8

'''
基准元素的原则：
    一般选择数组的第一个或最后一个元素
问题：假如有一个原本逆序的数列（以第一个元素为基准）/原本就是顺序的数列(以最后一个元素为基准)，这时候相当于每轮仅确定了一个基准元素的位置，时间复杂度退化为O(N^2)
解决办法：随机选择一个元素作为基准元素
'''

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def quickSort(array):
    '''
    分治思想
    每一轮挑选一个基准元素，并让其它比它大的元素移动到数组一侧，比它小的元素移动到另一侧
    平均情况下需要logN轮，平均时间复杂度为O(N*logN)
    '''
    if not array or len(array) < 2:
        return
    process(array, 0, len(array)-1)
    return

def process(array, start, end):
    if end > start:
        mid = partition(array, start, end)
        process(array, start, mid-1)
        process(array, mid+1, end)

def partition(array, left, right):
    '''
    荷兰国旗法
    以array[right]为key
    '''
    less, more, cur = left-1, right, left
    while cur < more:
        if array[cur] < array[right]:
            less += 1
            swap(array, cur, less)
            cur += 1
        elif array[cur] > array[right]:
            more -= 1
            swap(array, cur, more)
        else:
            cur += 1
    swap(array, cur, right)
    return cur

def partition(array, left, right):
    '''
    挖坑法，假设array[left]为空
    以array[left]为key
    '''
    if left >= right:
        return
    key = array[left]
    while left < right:
        while array[right] >= key and left < right:
            right -= 1
        if left < right:
            swap(array, left, right)
        while array[left] <= key and left < right:
            left += 1
        if left < right:
            swap(array, left, right)
    array[left] = key
    return left

def partition(array, left, right):
    '''
    指针交换法
    以array[left]为key
    '''
    if left >= right:
        return
    index = left
    key = array[left]
    while left < right:
        while array[right] > key and left < right:
            right -= 1
        while array[left] <= key and left < right:
            left += 1
        if left < right:
            swap(array, left, right)
    swap(array, left, index)
    return left


if __name__ == '__main__':
    array = [3, 1, 8, 10, 2, 9]
    quickSort(array)
    print(array)