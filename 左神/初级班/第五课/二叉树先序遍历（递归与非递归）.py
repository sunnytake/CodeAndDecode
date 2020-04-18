# coding=utf-8

def preOrderRecur(root):
    if not root:
        return []
    res = []
    res.append(root.val)
    res += preOrderRecur(root.left)
    res += preOrderRecur(root.right)
    return res

def inOrder(root):
    if not root:
        return []
    stack, res = [root], []
    while stack:
        node = stack.pop()
        res.append(node.val)
        # 先放入右子节点 => 后弹出
        if node.right:
            stack.append(node.right)
        # 后放入左子节点 => 先弹出
        if node.left:
            stack.append(node.left)
    return res