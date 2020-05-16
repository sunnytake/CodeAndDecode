# coding=utf-8
'''
给定一棵二叉树的头节点head和一个32位整数target，二叉树节点值类型为整型，求累加和为target的最长路径长度。
路径是指从某个节点往下，每次最多选择一个孩子节点或者不选所形成的的节点链
例如，对于如下二叉树
        -3
    3         -9
   1  0      2   1
     1   6
如果sum=6，那么累加和为6的最长路径为-3,3,0,6，所以返回4
如果sum=-9，那么累加和为-9的最长路径为-9，所以返回1
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

# 时间复杂度与空间复杂度均为O(N)
def getMaxLength(root, target):
    if not root:
        return 0
    # key为层，value为到当前层的和
    sum_level = {0: 0}
    return preOrder(root, target, 0, 1, 0, sum_level)

def preOrder(root, target, pre_sum, level, max_len, sum_level):
    if not root:
        return max_len
    cur_sum = pre_sum + root.val
    if cur_sum not in sum_level:
        sum_level[cur_sum] = level
    if (cur_sum - target) in sum_level:
        max_len = max(level-sum_level[cur_sum-target], max_len)
    max_len = preOrder(root.left, target, cur_sum, level+1, max_len, sum_level)
    max_len = preOrder(root.right, target, cur_sum, level + 1, max_len, sum_level)
    if level == sum_level[cur_sum]:
        sum_level.pop(cur_sum)
    return max_len














