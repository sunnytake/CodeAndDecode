# coding=utf-8
'''
给定一个有序数组，已知其中没有重复值，用这个有序数组生成一棵平衡搜索二叉树，
并且该搜索二叉树中序遍历结果于该数组一致

用有序数组最中间的数生成搜索二叉树的头节点，然后用这个数左边的数生成左子树，
用右边的数生成右子树
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def generateTree(array):
    if not array:
        return None
    return generate(array, 0, len(array)-1)

def generate(array, start, end):
    if start > end:
        return None
    mid = (start + end) >> 1
    root = Node(array[mid])
    root.left = generate(array, start, mid-1)
    root.right = generate(array, mid+1, end)
    return root















