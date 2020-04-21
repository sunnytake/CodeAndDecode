# coding=utf-8
'''
已知一棵完全二叉树，求其节点的个数
要求：时间复杂度小于O(N)，N为这棵树的节点个数
'''

'''
满二叉树的高度为L，节点个数为2^L-1
'''
def nodeNum(root):
    if not root:
        return 0
    return bs(root, 1, mostLeftLevel(root, 1))

# 获取当前节点左子树的深度
def mostLeftLevel(root, level):
    while root:
        level += 1
        root = root.left
    return level - 1

def bs(root, level, h):
    '''
    :param node:当前节点
    :param level: node所在层数
    :param h: 树的深度
    :return:
    '''
    if level == h:
        return 1
    if mostLeftLevel(root.right, level+1) == h:
        return (1 << (h-level)) + bs(root.right, level+1, h)
    else:
        return (1 << (h-level-1)) + bs(root.left, level+1, h)
