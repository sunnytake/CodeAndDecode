# coding=utf-8
'''
后序遍历二叉树，假设遍历到的当前节点为cur
'''
def nearstAncestor(root, node1, node2):
    if not root or node1 == root or node2 == root:
        return root
    left_ancestor = nearstAncestor(root.left, node1, node2)
    right_ancestor = nearstAncestor(root.right, node1, node2)
    if left_ancestor and right_ancestor:
        return root
    return left_ancestor if left_ancestor is not None else right_ancestor