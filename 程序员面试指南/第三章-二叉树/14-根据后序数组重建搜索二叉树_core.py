# coding=utf-8
'''
给定一个整形数组，已知其中没有重复值，判断arr是否可能是节点值类型为整数
的搜索二叉树后序遍历的结果。
进阶：如果整形数组中没有重复值，且已知是一棵搜索二叉树的后序遍历结果，通过
数组重建二叉树。
'''

def isPosArray(array):
    if not array:
        return False
    return isPos(array, 0, len(array)-1)

def isPos(array, start, end):
    if start == end:
        return True
    less, more = -1, end
    for i in range(start, end):
        if array[end] > array[i]:
            # array[end]为根节点,找到最后一个小于array[end]的位置
            less = i
        else:
            # 找到第一个大于array[end]的位置
            more = i if more == end else more

    # 全部大于根节点或全部小于根节点
    if less == -1 or more == end:
        return isPos(array, start, end-1)

    if less != more-1:
        return False
    return isPos(array, start, less) and isPos(array, more, end-1)

class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def posArrayToBST(array):
    if not array:
        return None
    return posToBST(array, 0, len(array)-1)

def posToBST(array, start, end):
    if start > end:
        return None
    root = Node(array[end])
    less, more = -1, end
    for i in range(start, end):
        if array[i] < array[end]:
            less += 1
        else:
            more = i if more == end else more
    root.left = posToBST(array, start, less)
    root.right = posToBST(array, more, end-1)
    return root