# coding=utf-8

def inOrderRecur(root, res):
    if not root:
        return res
    inOrderRecur(root.left, res)
    res.append(root.val)
    inOrderRecur(root.right, res)
    return res

def inOrderUnRecur(root):
    if not root:
        return []
    res = []
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            res.append(node.val)
            node = node.right
    return res




















