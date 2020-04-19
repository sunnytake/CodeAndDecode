# coding=utf-8

'''
二叉树按层遍历
1).如果有右孩子，无左孩子，不是
2).如果不是左右孩子都有（有左无右，左右都无），后面遇到的所有节点都必须是叶结点
3).不违反1和2，是
'''
def isFullTree(root):
    if not root:
        return True
    # 后续节点是否应该为叶结点
    state = False
    stack = [root]
    while stack:
        node = stack.pop(0)
        if (state and (node.left or node.right)) or (not node.left and node.right):
            return False
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        else:
            state = True
    return True