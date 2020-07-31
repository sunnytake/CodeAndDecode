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
class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

# 时间复杂度为O(N),空间复杂度为O(h->树的高度)
def getMaxLength(root, target):
    if not root:
        return 0
    # key为累加和，value为这个累加和最早出现的层数
    sum_level = {0: 0}
    return preOrder(root, target, 0, 1, 0, sum_level)

def preOrder(root, target, pre_sum, level, max_len, sum_level):
    if not root:
        return max_len
    cur_sum = pre_sum + root.val
    # 更新sum_level字典的原则：cur_sum第一次出现
    if cur_sum not in sum_level:
        sum_level[cur_sum] = level
    # 更新max_len的原则：cur_sum - target出现在sum_level中
    if (cur_sum - target) in sum_level:
        max_len = max(level-sum_level[cur_sum-target], max_len)
    max_len = preOrder(root.left, target, cur_sum, level + 1, max_len, sum_level)
    max_len = preOrder(root.right, target, cur_sum, level + 1, max_len, sum_level)
    if level == sum_level[cur_sum]:
        sum_level.pop(cur_sum)
    return max_len

if __name__ == '__main__':
    '''
            -3
    3         -9
   1  0      2   1
     1   6
    '''
    node1 = Node(-3)
    node2 = Node(3)
    node3 = Node(-9)
    node4 = Node(1)
    node5 = Node(0)
    node6 = Node(2)
    node7 = Node(1)
    node8 = Node(1)
    node9 = Node(6)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node5.left = node8
    node5.right = node9
    print(getMaxLength(node1, 6))
    print(getMaxLength(node1, -9))











