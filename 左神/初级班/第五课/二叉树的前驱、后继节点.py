# coding=utf-8

"""
二叉树前驱节点和后继节点：一个二叉树中序遍历中某个节点的前一个节点叫该节点的前驱节点，某个节点的后一个节点叫后继节点
该题目中还有一个节点指向节点的父节点 parent，规定头节点的父亲节点的指针为空。
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.parent = None, None, None


def nextNode(node):
    # 如果有右子树，返回右子树的最左结点
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    # 无子节点
    elif node.parent:
        # 若该节点不存在右子树，则利用parent指针向父节点找，
        # 若满足该节点是其父节点的左节点，则该父节点为当前节点的后继节点，
        # 若不满足则更新父节点为祖父节点，当前节点更新为其父节点，
        # 直到满足条件或者父亲节点为空，为空表示到达根节点依旧没有找到。
        parent = node.parent
        while parent and parent.left != node:
            node = parent
            parent = node.parent
        return parent
    return None

def preNode(node):
    # 如果有左子树，则为左子树最右节点
    if node.left:
        node = node.left
        while node.right:
            node = node.right
        return node
    # 若该节点不存在左子树，则利用parent指针向父节点找，
    # 若满足该节点是其父节点的右节点，则该父节点为当前节点的前驱节点，
    # 若不满足则更新父节点为祖父节点，当前节点更新为其父节点，
    # 直到满足条件或者父节点为空，为空表示到达根节点依旧没有找到。
    elif node.parent:
        parent = node.parent
        while parent and parent.right != node:
            node = parent
            parent = node.parent
        return parent
    return None
