# coding=utf-8
'''
给定彼此独立的两棵树头节点分别为t1和t2，判断t1树是否包含t2树的全部拓扑结构。
例如，下面t1树包含t2树
t1树：
        1
     2        3
 4       5  6   7
8  9   10
t2树:
    2
  4   5
8
'''
# 时间复杂度为O(NxM)
def contains(root1, root2):
    return check(root1, root2) or contains(root1.left, root2) or contains(root1.right, root2)

def check(root1, root2):
    if not root2:
        return True
    if not root1 or root1.val != root2.val:
        return False
    return check(root1.left, root2.left) and check(root1.right, root2.right)