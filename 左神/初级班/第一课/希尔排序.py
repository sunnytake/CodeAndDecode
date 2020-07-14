# coding=utf-8

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def shellSort(array):
    '''
    逐步分组进行粗调，再进行直接插入排序
    利用分组粗调的方式减少了直接插入排序的工作量，使得算法的平均时间复杂度低于O(n^2)
    但是，在某些极端情况下，希尔排序的最坏时间复杂度仍然是O(n^2)，甚至比直接插入排序更慢（增加了分组的成本）。
    例如：2    1   5   3   7   6   9   8
    无论以4为增量，还是以2为增量，每组内部的元素都没有任何交换，一直到把增量缩减为1，数组才会按照直接插入排序的方式进行调整
    导致这种极端情况的原因：每一轮希尔排序之间是等比的
    解决方案：为了保证分组粗调没有盲区，每一轮的增量需要彼此互质，也就是没有除1之外的公约数
    不稳定
    https://mp.weixin.qq.com/s?__biz=MzIxMjE5MTE1Nw==&mid=2653199674&idx=1&sn=9ab7bb7e465104c67a3d8590ebd0fe6c&chksm=8c99efe0bbee66f69c07e5f423d7751c9667fa82beb6dcaef4c0e96dac9545d2277c8179c765&scene=21#wechat_redirect
    '''
    if not array or len(array) < 2:
        return
    d = len(array)
    while d > 1:
        # 使用希尔增量的方式，每次折半
        d = d // 2
        for x in range(0, d):
            for i in range(x+d, len(array), d):
                temp = array[i]
                j = i - d
                while j >= 0 and array[j] > temp:
                    array[j+d] = array[j]
                    j -= d
                array[j + d] = temp
    return


if __name__ == '__main__':
    array = [3, 1, 8, 10, 2, 9]
    shellSort(array)
    print(array)