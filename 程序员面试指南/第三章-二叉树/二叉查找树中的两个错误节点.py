# coding=utf-8
'''
一棵二叉树原本是搜索二叉树，但是其中有两个节点调换了位置，使得这棵二叉树不
再是搜索二叉树，请找到这两个错误节点并返回。已知二叉树中所有节点的值都不一样，
给定二叉树的头节点root，返回二叉树的错误节点
进阶：如果在原问题中得到了这两个错误节点，我们当然可以通过交换两个节点的节点值
的方式让整棵二叉树重新成为搜索二叉树。但现在要求不能这么做，而是在结构上完全交
换两个节点的位置，请实现调整的函数。
情况特别多：
问题1：e1和e2是否有一个是头节点？如果有，谁是头？
问题2：e1和e2是否相邻？如果相邻，谁是谁的父节点？
问题3：e1和e2分别是各自父节点的左孩子还是右孩子？
特别注意：因为是在中序遍历时先找到e1，后找到e2，所以e1一定不是e2的右孩子，
e2也一定不是e1的左孩子
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def getErrorNodes(root):
    if not root:
        return []
    errors = []
    stack = []
    pre = None
    node = root
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if pre and pre.val > node.val:
                errors.append(node)
            pre = node
            node = node.right
    return errors

def getErrorParents(root, err1, err2):
    parents = [None, None]
    if not root:
        return parents

    node = root
    stack = []
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.left == err1 or node.right == err1:
                parents[0] = node
            if node.left == err2 or node.right == err2:
                parents[1] = node
            node = node.right
    return parents
























