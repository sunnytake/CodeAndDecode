# coding=utf-8

def preOrderRecur(root):
    if not root:
        return []
    res = [root.val]
    res += preOrderRecur(root.left)
    res += preOrderRecur(root.right)
    return res

def preOrderUnRecur(root):
    if not root:
        return []
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

























