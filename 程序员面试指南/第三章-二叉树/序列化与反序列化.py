# coding=utf-8
'''
二叉树被记录为文件的过程叫做二叉树的序列化，通过文件内容重建原来二叉树的过程叫做二叉树的反序列化
给定一棵二叉树的头节点head，并已知二叉树节点值的类型为32位整型，
请设计一种二叉树序列化和反序列化的方案，并用代码实现
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

# 先序序列化
def serialByPre(root):
    if not root:
        return '#!'
    res = str(root.val) + '!'
    res += serialByPre(root.left)
    res += serialByPre(root.right)
    return res

# 先序反序列化
def deserialByPre(string):
    def build(values):
        value = values.pop(0)
        if value == '#':
            return None
        root = Node(int(value))
        root.left = build(values)
        root.right = build(values)
        return root
    values = string.split('!')
    return build(values)

# 层次遍历序列化
def serialByLevel(root):
    if not root:
        return '#!'
    res = root.val + '!'
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left:
            res += node.left.val + '!'
            queue.append(node.left)
        else:
            res += '#!'
        if node.right:
            res += node.right.val + '!'
            queue.append(node.right)
        else:
            res += '#!'
    return res

# 层次反序列化
def deserialByLevel(string):
    def generateNode(val):
        if val == '#':
            return None
        return Node(val)
    values = string.split('!')
    root = generateNode(values[0])
    index = 1
    queue = []
    if root:
        queue.append(root)
    while queue:
        node = queue.pop(0)
        node.left = generateNode(values[index])
        index += 1
        node.right = generateNode(values[index])
        index += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return root




































