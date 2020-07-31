# coding=utf-8

def inOrderRecur(root):
    if not root:
        return []
    res = []
    res += inOrderRecur(root.left)
    res.append(root.val)
    res += inOrderRecur(root.right)
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




















