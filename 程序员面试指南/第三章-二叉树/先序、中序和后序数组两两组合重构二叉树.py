# coding=utf-8
'''
已知一棵二叉树的所有节点值都不同，给定这棵二叉树正确的先序、中序和后序数组。
请分别用三个函数实现任意两种数组组合重构原来的二叉树，并返回重构二叉树的头节点
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def preInToTree(pre_vals, in_vals):
    if not pre_vals or not in_vals:
        return None
    val = pre_vals[0]
    index = in_vals.index(val)
    root = Node(val)
    root.left = preInToTree(pre_vals[1:index+1], in_vals[:index])
    root.right = preInToTree(pre_vals[index+1:], in_vals[index+1:])
    return root

def inPosToTree(in_vals, pos_vals):
    if not in_vals or not pos_vals:
        return None
    val = pos_vals[0]
    index = in_vals.index(val)
    root = Node(val)
    root.left = preInToTree(in_vals[:index], pos_vals[:index])
    root.right = preInToTree(in_vals[index+1:], pos_vals[index: -1])
    return root

'''
先序与后序构建二叉树：
即便得到了正确的先序与后序数组，大多数情况下也不能通过这两个数组重构原来的树。
这是因为在很多结构不同的树中，先序与后序数组是一样的。比如：
    1
2       None
先序为[1,2]，后序为[2,1]
而：
    1
None    2
先序为[1,2]，后序为[2,1]
这两棵结构不同的树先序与后序数组一样。
什么树可以被先序和后序数组重建？
如果一棵二叉树除叶节点之外，其它所有的节点都有左孩子和右孩子，
只有这样的树才可以被先序和后序数组重构。
'''
def prePosToTree(pre_vals, pos_vals):
    if not pre_vals or not pos_vals:
        return None
    val = pre_vals[0]
    root = Node(val)
    index = pos_vals.index(pre_vals[1])
    root.left = prePosToTree(pre_vals[1: index+2], pos_vals[:index+1])
    root.right = prePosToTree(pre_vals[index+2:], pos_vals[index+1:-1])
    return root






















