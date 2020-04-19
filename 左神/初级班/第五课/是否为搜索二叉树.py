# coding=utf-8

'''
方法1：
可以层次遍历，从上到下依次判断是否左小右大
方法2：
借助中序遍历的思想
'''
def isSearchTree(root):
    if not root:
        return True
    stack = []
    pre_val = None
    node = root
    while node or stack:
        if node:
            stack.append(node)
        else:
            node = stack.pop()
            # 中序遍历的下一个节点
            if pre_val and node.val < pre_val:
                return False
            node = node.right
    return True
