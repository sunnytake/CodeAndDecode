# coding=utf-8

"""
最大路径长度（边的个数）
"""
def maxPath(root):
    if not root:
        return -1
    max_length = float('-inf')
    def getMax(root):
        global max_length
        left_len, right_len = 0, 0
        if root.left:
            # 1为root到root.left之间的边的权值
            left_len = getMax(root.left) + 1
        if root.right:
            # 1为root到root.right之间的边的权值
            right_len = getMax(root.right) + 1
        sum_length = left_len + right_len
        max_length = sum_length if sum_length > max_length else max_length
        # 返回值为单结点深度，即只能为左子树或右子树的深度
        return left_len if left_len >= right_len else right_len
    getMax(root)
    return max_length

"""
最大路径和，边经过结点的值求和
"""
def maxPath2(root):
    if not root:
        return None
    max_sum = float('-inf')
    def getMax(root):
        global max_sum
        left_sum, right_sum = 0, 0
        if root.left:
            left_sum = getMax(root.left) + root.val
        if root.right:
            right_sum = getMax(root.right) + root.val
        total_sum = left_sum + right_sum
        max_sum = total_sum if total_sum > max_sum else max_sum
        return left_sum if left_sum >= right_sum else right_sum
    maxPath2(root)
    return max_sum