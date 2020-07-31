# coding=utf-8
'''
二叉树中序遍历的下一个节点叫做后继节点
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.parent = None, None, None


def getNextNode(node):
    if not node:
        return node
    if node.right:
        return getLeftMost(node.right)
    else:
        parent = node.parent
        while parent and parent.left != node:
            node = parent
            parent = node.parent
        return parent

def getLeftMost(root):
    if not root:
        return root
    while root.left:
        root = root.left
    return root