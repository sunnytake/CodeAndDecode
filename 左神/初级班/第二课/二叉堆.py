# coding=utf-8
'''
小顶堆
'''

def upAdjust(array):
    '''
    上浮调整
    '''
    child_index = len(array) - 1
    parent_index = (len(array) - 1) // 2
    # temp保存插入的叶子节点值，用于最后的赋值
    temp = array[child_index]
    while parent_index >= 0 and temp < array[parent_index]:
        # 无需真正交换，单向赋值即可
        array[child_index] = array[parent_index]
        child_index = parent_index
        parent_index = (child_index - 1) // 2
    array[child_index] = temp


def downAdjust(array, parent_index, length):
    '''
    下沉调整
    :param array: 待调整的堆
    :param parent_index: 要下沉的父节点
    :param length: 堆的有效大小
    '''
    # temp保存父节点的值，用于最后的赋值
    temp = array[parent_index]
    child_index = 2 * parent_index + 1
    while child_index < length:
        if child_index + 1 < length and array[child_index + 1] < array[child_index]:
            child_index += 1
        if temp <= array[child_index]:
            break
        array[parent_index] = array[child_index]
        parent_index = child_index
        child_index = 2 * child_index + 1
    array[parent_index] = temp


def buildHeap(array):
    '''
    构建堆
    :param array: 待调整的堆
    '''
    # 从最后一个非叶子节点开始，依次下沉调整
    for index in range(len(array) // 2, -1, -1):
        downAdjust(array, index, len(array))


if __name__ == '__main__':
    array = [1, 3, 2, 6, 5, 7, 8, 9, 10, 0]
    upAdjust(array)
    print('up adjust', array)

    array = [7, 1, 3, 10, 5, 2, 8, 9, 6]
    buildHeap(array)
    print('build heap', array)



















