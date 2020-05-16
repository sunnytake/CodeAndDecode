# coding=utf-8
'''
给定一棵二叉树的头节点head，已知其中所有节点的值都不一样，
找到含有节点最多的搜索二叉子树，并返回这棵子树的头节点
例如，对于如下二叉树
        6
    1               12
  0   3       10            13
            4     14     20    16
          2  5  11  15
则这棵树中的最大搜索二叉树为以10为根节点的二叉树
如果不要求空间复杂度为O(h)，则可以将问题转化为中序遍历二叉树，找到最长的单调递增子数组即可
'''

'''
以节点node为头的树中，最大的搜索二叉子树只可能来自以下两种情况：
1. 如果来自node左子树上的最大搜索二叉子树是以node.left为头的；来自node
右子树上的最大搜索二叉子树是以node.right为头的；node左子树上的最大搜索
二叉子树的最小值小于node.val；node右子树上的最大搜索二叉子树的最小值大于
node.val，那么以节点node为头的整棵树都是搜索二叉树
2.如果不满足条件1，说明以节点node为头的树整体不能连成搜索二叉树。这种情况下，
以node为头的树上的最大搜索二叉子树是来自node的左子树上的最大搜索二叉子树和来自
node的右子树上的最大搜索二叉子树之间，节点数较多的那个

具体过程如下:
1.整体过程是二叉树的后序遍历
2.遍历到当前节点cur时，先遍历cur的左子树收集4个信息，分别时左子树上
最大搜索二叉子树的头节点(lBst)，节点数(left_size)，最小值(left_min)和
最大值(left_max)。再遍历cur的右子树收集4个信息，分别是右子树上最大搜索
二叉子数的头节点(rBst)，节点数(right_size)，最小值(right_min)，最大值(right_max)
3.根据步骤2收集的信息，判断是否满足第1中情况，如果满足，则返回cur节点，否则返回lBst和rBst中较大的
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def getBiggestSubBst(root):
    # 分别记录节点数，最小值，最大值
    record = [None, None, None]
    return posOrder(root, record)

def posOrder(root, record):
    if not root:
        return None
    lBst = posOrder(root.left, record)
    left_size, left_min, left_max = record
    rBst = posOrder(root.right, record)
    right_size, right_min, right_max = record
    record[1] = min(left_min, root.val)
    record[2] = max(right_max, root.val)
    if root.left == lBst and root.right == rBst and (not left_max or left_max < root.val) and (not right_min or root.val < root.val):
        record[0] = left_size + right_size + 1
        return root
    record[0] = max(left_size, right_size)
    return root.left if left_size >= right_size else root.right
