# coding=utf-8

# 二叉树序列化
def serialByPre(root):
    '''
    结点之间用!分割，用#表示空结点
    :param root:
    :return:
    '''
    if not root:
        return "#!"
    res = root.val + '!'
    res += serialByPre(root.left)
    res += serialByPre(root.right)
    return res

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 二叉树反序列化
def reconByPreString(pre_str):
    values = pre_str.split('!')
    return reconPreOrder(values)

def reconPreOrder(values):
    value = values.pop(0)
    if value == '#':
        return None
    root = Node(int(value))
    root.left = reconPreOrder(values)
    root.right = reconPreOrder(values)
    return root