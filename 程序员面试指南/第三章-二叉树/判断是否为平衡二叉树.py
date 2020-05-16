# coding=utf-8
'''
平衡二叉树的性质为：要么是一棵空树，要么任何一个节点的左右子树高度差的绝对值不超过1。
给定一棵二叉树的头节点root，判断这棵二叉树是否为平衡二叉树
'''

def isBalance(root):
    res = [True]
    getHeight(root, 1, res)
    return res[0]

def getHeight(root, level, res):
    if not root:
        return level
    left_height = getHeight(root.left, level+1, res)
    if not res[0]:
        return level
    right_height = getHeight(root.right, level+1, res)
    if not res[0]:
        return level
    if abs(left_height-right_height) > 1:
        res[0] = False
    return max(left_height, right_height)