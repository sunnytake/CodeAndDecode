# coding=utf-8

def levelOrder(root):
    if not root:
        return []
    queue, res = [root], []
    while queue:
        node = queue.pop(0)
        res.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res