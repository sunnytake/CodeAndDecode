# coding=utf-8

'''
给定一个二叉树的头节点head，已知其中没有重复值的节点，实现两个函数分别判断
这棵二叉树是否为搜索二叉树和二叉完全树
'''

def isSearchTree(root):
    if not root:
        return True
    left = isSearchTree(root.left)
    if not left:
        return False
    right = isSearchTree(root.right)
    if not right:
        return False
    res = True
    if root.left:
        res = root.left.val < root.val
    if root.right:
        res = res and root.val < root.right.val
    return res


def isSearchTree(root):
    if not root:
        return True
    pre = None
    node = root
    stack = []
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if pre and pre > node.val:
                return False
            pre = node.val
    return True

def isFullTree(root):
    if not root:
        return True
    stack = [root]
    leaf = False
    while stack:
        node = stack.pop(0)
        if (leaf and (node.left or node.right)) or (not node.left and node.right):
            return False
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        else:
            leaf = True
    return True










