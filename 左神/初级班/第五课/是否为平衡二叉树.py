# coding=utf-8

'''
我的方法
'''
def isBalanceTree(root):
    if not root:
        return True
    left_balance = isBalanceTree(root.left)
    right_balance = isBalanceTree(root.right)
    if left_balance and right_balance:
        left_length = getLength(root.left)+1
        right_length = getLength(root.right)+1
        if abs(left_length - right_length) <= 1:
            return True
    return False

def getLength(root):
    if not root:
        return 0
    left_length = getLength(root.left)
    right_length = getLength(root.right)
    return max(left_length, right_length)+1

'''
左神的方法：树形BP
'''
def isBalanceTree(root):
    return process(root)[0]

def process(root):
    '''
    递归要两个结果：1：二叉树的高度 2.是否为二叉树
    :param root:
    :return:
    '''
    if not root:
        # 第一位代表是否平衡，第二位为深度
        # 当不平衡时，第二位无用，填充0即可
        return (True, 0)
    left_res = process(root.left)
    if not left_res[0]:
        return (False, 0)
    right_res = process(root.right)
    if not right_res[0]:
        return (False, 0)
    if abs(left_res[1] - right_res[1]) > 1:
        return (False, 0)
    return (True, max(left_res[1], right_res[1])+1)

