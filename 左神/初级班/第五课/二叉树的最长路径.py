# coding=utf-8

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
    仅仅返回长度，同层次遍历
    :param root:
    :return:
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


