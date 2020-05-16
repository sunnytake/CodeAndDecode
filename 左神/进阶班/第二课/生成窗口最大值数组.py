"""
有一个整型数组arr和一个大小为w的窗口从数组的最左边滑到最右边
窗口每次向右滑一个位置
例如，数组为[4,3,5,4,3,3,6,7]，窗口大小为3时：
[4 5 5] 4 3 3 6 7   窗口中最大值为5
4 [3 5 4] 3 3 6 7   窗口中最大值为5
4 3 [5 4 3] 3 6 7   窗口中最大值为5
4 3 5 [4 3 3] 6 7   窗口中最大值为4
4 3 5 4 [3 3 6] 7   窗口中最大值为6
4 3 5 4 3 [3 6 7]   窗口中最大值为7
如果数组长度为n，窗口大小为w，则一共产生n-w+1个窗口的最大值
请实现一个函数：
    输入：整型数组arr，窗口大小为w
    输出：一个长度为n-w+1的数组res, res[i]表示每一种窗口状态下的最大值
"""
def getMaxArray(array, w):
    if not array or w < 1 or len(array) < w:
        return []
    max_array = []
    res = []
    for i in range(len(array)):
        while max_array and array[max_array[-1]] <= array[i]:
            max_array.pop(-1)
        max_array.append(i)
        if max_array[0] == i - w:
            max_array.pop(0)
        if i >= w - 1:
            res.append(array[max_array[0]])
    return res

if __name__ == '__main__':
    array = [4,3,5,4,3,3,6,7]
    w = 3
    print(getMaxArray(array, w))