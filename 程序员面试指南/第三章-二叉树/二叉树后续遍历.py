# coding=utf-8

def posOrderRecur(root, res):
    if not root:
        return res
    posOrderRecur(root.left, res)
    posOrderRecur(root.right, res)
    res.append(root.val)
    return res

def posOrderUnRecur1(root):
    if not root:
        return []
    res = []
    stack1 = [root]
    while stack1:
        node = stack1.pop()
        res.append(node.val)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    return res[::-1]































