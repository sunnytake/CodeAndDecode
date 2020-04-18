# coding=utf-8

def posOrderRecur(root):
    if not root:
        return []
    res = []

    res += posOrderRecur(root.left)
    res += posOrderRecur(root.right)
    res.append(root.val)
    return res

def posOrder(root):
    if not root:
        return []
    stack1, res = [root], [],
    while stack1:
        node = stack1.pop()
        res.append(node.val)
        # 先压入左子树 => 先弹出
        if node.left:
            stack1.append(node.left)
        # 后压入右子树 => 后弹出
        if node.right:
            stack1.append(node.right)

    return res[::-1]