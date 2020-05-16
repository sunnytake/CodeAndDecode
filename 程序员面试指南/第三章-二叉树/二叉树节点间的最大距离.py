# coding=utf-8
'''
从二叉树的节点A出发，可以向上或者向下走，但是沿途的节点只能经过一次，
当到达节点B时，路上的节点数叫做A到B的距离
'''

def getMaxDistance(root):
    res = [None]
    return posOrder(root, res)

def posOrder(root, res):
    if not root:
        res[0] = 0
        return 0
    # 经过左子树的最大距离
    left_max = posOrder(root.left, res)
    # 左子树的深度
    left_length = res[0]
    right_max = posOrder(root.right, res)
    right_length = res[0]
    cur_max = left_length + right_length + 1
    res[0] = max(left_length, right_length) + 1
    return max(max(left_max, right_max), cur_max)
