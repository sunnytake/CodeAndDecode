# coding=utf-8

def inOrderRecur(root):
    if not root:
        return []
    res = []
    res += inOrderRecur(root.left)
    res.append(root.val)
    res += inOrderRecur(root.right)
    return res

def preOrder(root):
    if not root:
        return []
    stack, res = [], []
    node = root
    while node or stack:
        # 不空压入栈，当前节点向左
        if node:
            stack.append(node)
            node = node.left
        # 当前节点为空，从栈拿一个，打印，当前节点向右
        else:
            node = stack.pop()
            res.append(node.val)
            node = node.right
    return res