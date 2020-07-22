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
    return bs(root, 1, mostLeftLevel(root, 0))

# 获取当前节点左子树的深度
def mostLeftLevel(root, level):
    while root:
        level += 1
        root = root.left
    return level

def bs(root, level, h):
    '''
    :param node:当前节点
    :param level: node所在层数
    :param h: 树的深度
    :return:
    '''
    # 最后一层，没有子节点，则为1
    if level == h:
        return 1
    # 如果右子树的深度等于树的深度，则左子树一定是满的
    if mostLeftLevel(root.right, level+1) == h:
        # 左子树为高度为high-level的满二叉树，则节点数为2^(high-level) - 1个
        # 右子树高度不确定，节点个数为bs(root.right, level+1, h)
        # 总节点个数为 2^(high-level) - 1 + bs(root.right, level+1, high) + 1(当前节点)
        return (1 << (h-level)) + bs(root.right, level+1, h)
    # 如果右子树深度不等于树的深度，则左子树不一定是满的
    else:
        # 左子树高度不确定，节点个数为bs(root.left, level+1, h)
        # 右子树高度肯定为high-1，则节点个数为2^(high-level-1) - 1个
        # 总节点个数为bs(root.left, level+1, high) + 2^(high-level-1) - 1 + 1（当前节点）
        return (1 << (h-level-1)) + bs(root.left, level+1, h)
