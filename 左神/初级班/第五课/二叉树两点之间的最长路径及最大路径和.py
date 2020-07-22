# coding=utf-8

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def process_length(root, max_length):
    '''
    二叉树中经过某一节点的最大路径长度
    '''
    left_length, right_length = 0, 0
    if root.left:
        # 1为root到root.left之间的边的权值
        left_length = process_length(root.left, max_length) + 1
    if root.right:
        # 1为root到root.right之间的边的权值
        right_length = process_length(root.right, max_length) + 1
    total_length = left_length + right_length
    max_length[0] = total_length if total_length > max_length[0] else max_length[0]
    # 返回值为单结点深度，即只能为左子树或右子树的深度
    return left_length if left_length >= right_length else right_length


def process_sum(root, max_sum):
    '''
    二叉树中经过某一节点的最大路径和
    '''
    left_sum, right_sum = 0, 0
    if root.left:
        left_sum = process_sum(root.left, max_sum) + root.left.val
    if root.right:
        right_sum = process_sum(root.right, max_sum) + root.right.val
    total_sum = left_sum + right_sum + root.val
    max_sum[0] = total_sum if total_sum > max_sum[0] else max_sum[0]
    return left_sum if left_sum >= right_sum else right_sum


def maxPath(root):
    if not root:
        return -1
    max_length = [0]
    process_length(root, max_length)
    max_sum = [0]
    process_sum(root, max_sum)
    return max_length[0], max_sum[0]


if __name__ == '__main__':
    '''
    构造树
                1
             2
          3     4
                   5
                10    6
    最长路径：3 -> 2 -> 4 -> 5 -> 6/10，共有4条边
    最长路径和：3 -> 2 -> 4 -> 5 -> 10，和为3+2+4+5+10=24
    '''
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node10 = TreeNode(10)
    node1.left = node2
    node2.left = node3
    node2.right = node4
    node4.left = node5
    node5.left = node10
    node5.right = node6
    print(maxPath(node1))






















