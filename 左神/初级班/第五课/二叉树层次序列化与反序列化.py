# coding=utf-8

def serialByLevel(root):
    if not root:
        return '#!'
    res = root.val + '!'
    stack = [root]
    while stack:
        node = stack.pop(0)
        if node.left:
            res += root.left.val + '!'
            stack.append(node.left)
        else:
            res += '#!'
        if node.right:
            res += root.right.val + '!'
            stack.append(node.right)
        else:
            res += '#!'
    return res

class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def reconByLevelString(level_str):
    values = level_str.split('!')

    index = 0
    root = generateNodeByString(values[index])
    index += 1

    stack = []
    if root:
        stack.append(root)
    while stack:
        node = stack.pop(0)
        node.left = generateNodeByString(values[index])
        index += 1
        node.right = generateNodeByString(values[index])
        index += 1
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return root

def generateNodeByString(val):
    if val == '#':
        root = None
    else:
        root = Node(int(val))
