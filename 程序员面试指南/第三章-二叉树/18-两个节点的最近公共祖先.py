# coding=utf-8
'''
给定一棵二叉树的头节点head，以及这棵树中的两个节点o1和o2，请返回o1和o2的最近公共祖先节点。
            1
        2        3
      4   5   6    7
                  8
节点4和节点5的最近公共祖先节点为节点2，节点5和2的最近公共祖先节点为节点2，
节点6和8的最近公共祖先节点为节点3，节点5和节点8的最近公共祖先节点为节点1

进阶：如果查询两个节点的最近公共祖先操作十分频繁，如何让单挑查询的查询时间减少
再进阶：给定二叉树的根节点root，同时给定所有想要进行的查询。二叉树的节点数量为N，
查询条数为M，请在时间复杂度为O(N+M)内返回所有查询的结果。
'''
def nearstAncestor(root, node1, node2):
    if not root or node1 == root or node2 == root:
        return root
    left_ancestor = nearstAncestor(root.left, node1, node2)
    right_ancestor = nearstAncestor(root.right, node1, node2)
    if left_ancestor and right_ancestor:
        return root
    return left_ancestor if left_ancestor else right_ancestor


# 进阶版本：建立记录的时间复杂度为O(N)，额外空间复杂度为O(N)，查找的时间复杂度为O(h)
class Record1:
    def __init__(self, root):
        self.map = {}
        if root:
            self.map[root] = None
        self.setMap(root)

    def setMap(self, root):
        if not root:
            return
        if root.left:
            self.map[root.left] = root
        if root.right:
            self.map[root.right] = root
        self.setMap(root.left)
        self.setMap(root.right)

    def query(self, node1, node2):
        path = []
        while node1 in self.map[node1]:
            path.append(node1)
            node1 = self.map[node1]
        while node2 not in path:
            node2 = self.map[node2]
        return node2

# 再进阶版本：直接建立任意两个节点之间的公共祖先记录，便于后续查找
class Record2:
    '''
    建立记录的过程：
    1. 对二叉树中的每棵子树（一共N棵）都进行步骤2
    2. 假设子树的头节点为root，root所有的后代节点和root节点的最近公共祖先都是root，记录下来。
    root左子树的每个节点和root右子树的每个节点的最近公共祖先都是root，记录下来。
    '''
    def __init__(self, root):
        self.map = {}
        self.initMap(root)
        self.setMap(root)

    def initMap(self, root):
        if not root:
            return
        self.map[root] = {}
        self.initMap(root.left)
        self.initMap(root.right)

    def setMap(self, root):
        if not root:
            return
        self.rootRecord(root.left, root)
        self.rootRecord(root.right, root)
        self.subRecord(root)
        self.setMap(root.left)
        self.setMap(root.right)

    def rootRecord(self, node, root):
        if not node:
            return
        self.map[node][root] = root
        self.rootRecord(node.left, root)
        self.rootRecord(node.right, root)

    def subRecord(self, root):
        if not root:
            return
        self.preLeft(root.left, root.right, root)
        self.subRecord(root.left)
        self.subRecord(root.right)

    def preLeft(self, left, right, root):
        if not left:
            return
        self.preRight(left, right, root)
        self.preLeft(left.left, right, root)
        self.preLeft(left.right, right, root)

    def preRight(self, left, right, root):
        if not right:
            return
        self.map[left][right] = root
        self.preRight(left, right.left, root)
        self.preRight(left, right.right, root)

    def query(self, node1, node2):
        if node1 == node2:
            return node1
        if node1 in self.map:
            return self.map[node1][node2]
        if node2 in self.map:
            return self.map[node2][node1]
        return None