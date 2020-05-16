# coding=utf-8
'''
给定一棵二叉树的头节点head，已知所有节点的值都不一样，返回其中最大的且符合搜索
二叉树条件的最大拓扑结构的大小
例如，对于如下二叉树
        6
    1               12
  0   3       10            13
            4     14     20    16
          2  5  11  15
最大且符合搜索二叉树的最大拓扑结构如下：
              6
    1               12
  0   3       10            13
                               16
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

# 时间复杂度为O(N^2)
def bstTopoSize(root):
    if not root:
        return 0
    max_size = maxTopo(root, root)
    max_size = max(bstTopoSize(root.left), max_size)
    max_size = max(bstTopoSize(root.right), max_size)
    return max_size

def maxTopo(root, node):
    if root and node and isBstNode(root, node):
        return maxTopo(root, node.left) + maxTopo(root, node.right)+1
    return 0

def isBstNode(root, node):
    if not root:
        return False
    if root == node:
        return True
    if node.val > root.val:
        return isBstNode(root.right, node)
    else:
        return isBstNode(root.left, node)

class Record:
    def __init__(self, left, right):
        self.left, self.right = left, right

# 方法2：最好的时间复杂度为O(N)，最坏为O(NlogN)
def bstTopoSize2(root):
    # 键为节点，值为拓扑贡献表
    # 第一个值代表节点的左子树可以为当前头节点的拓扑贡献几个节点
    # 第二个值代表节点的右子树可以为当前头节点的拓扑贡献几个节点
    node_record = {}
    return posOrder(root, node_record)

def posOrder(root, node_record):
    if not root:
        return 0
    left_max = posOrder(root.left, node_record)
    right_max = posOrder(root.right, node_record)
    modifyMap(root.left, root.val, node_record, True)
    modifyMap(root.right, root.val, node_record, False)
    left_record = node_record[root.left]
    right_record = node_record[root.right]
    left_bst = 0 if left_record is None else left_record.left + left_record.right + 1
    right_bst = 0 if right_record is None else right_record.left + right_record.right + 1
    node_record[root] = Record(left_bst, right_bst)
    return max(left_bst+right_bst+1, max(left_max, right_max))

def modifyMap(child, root_val, node_record, left_child_flag):
    if not child or child not in node_record:
        return 0
    record = node_record[child]
    # 左子树找比根大的，右子树找比根小的，这些节点需要删除
    if (left_child_flag and child.val > root_val) or (not left_child_flag and child.val < root_val):
        node_record.pop(child)
        return record.left + record.right + 1
    else:
        if left_child_flag:
            minus = modifyMap(child.right, root_val, node_record, left_child_flag)
            record.right -= minus
        else:
            minus = modifyMap(child.left, root_val, node_record, left_child_flag)
            record.left -= minus
        node_record[child] = record
        return minus

