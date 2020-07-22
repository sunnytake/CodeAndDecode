# coding=utf-8

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

"""
在一个二叉树中，输出从根节点到叶子节点的最长路径。
"""
def getLongestPathRecur(root):
    if not root:
        return []
    else:
        left_path = getLongestPathRecur(root.left)
        right_path = getLongestPathRecur(root.right)
        return [root] + left_path if len(left_path) >= len(right_path) else [root]+right_path


def getLongestPath(root):
    '''
    仅仅返回路径上的节点个数，同层次遍历
    '''
    if not root:
        return []
    queue = [root]
    # 记录当层有多少个节点，以及目前遍历到哪个节点
    level_num, level_now = 1, 0
    depth = 0
    while queue:
        node = queue.pop(0)
        level_now += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        if level_now == level_num:
            depth += 1
            level_now = 0
            level_num = len(queue)
    return depth

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
    print([node.val for node in getLongestPathRecur(node1)])
    print(getLongestPath(node1))

