# coding=utf-8
'''
给定一棵完全二叉树的头节点head，返回这棵树的节点个数
'''

# 时间复杂度O(logN)*O(logN)
def countNodes(root):
    left, right = root, root
    left_level, right_level = 0, 0
    while left:
        left = left.left
        left_level += 1
    while right:
        right = right.right
        right_level += 1
    if left_level == right_level:
        return 2 ** left_level - 1
    return 1 + countNodes(root.left) + countNodes(root.right)


# 时间复杂度O(h^2)
def countNodes2(root):
    if not root:
        return 0
    return bs(root, 1, mostLeftLevel(root, 1))

def bs(root, low, high):
    if low == high:
        return 1
    if mostLeftLevel(root.right, low+1) == high:
        return 2 ^ (high - low) + bs(root.right, low+1, high)
    else:
        return 2 ^ (high - low - 1) + bs(root.left, low+1, high)

def mostLeftLevel(root, level):
    while root.left:
        level += 1
        root = root.left
    return level
