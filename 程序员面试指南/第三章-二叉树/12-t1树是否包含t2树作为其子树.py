# coding=utf-8
'''
给定彼此独立的两棵树头节点分别为t1和t2，判断t1中是否有与t2拓扑结构完全相同的子树
例如，如下两棵树
t1:
           1
     2            3
  4      5    6       7
     8 9
t2:
      2
 4          5
     8  9
t1树有与t2树拓扑结构完全相同的子树，所以返回true

先序遍历+KMP
'''


def contain(root1, root2):
    '''
    时间复杂度为O(NxM)：root1的节点数 x root2的节点数
    '''
    return process(root1, root2) or process(root1.left, root2) or process(root1.right, root2)


def process(root1, root2):
    if not root1 and not root2:
        return True
    if root1 and root2 and root1.val == root2.val:
        return process(root1.left, root2.left) and process(root1.right, root2.right)
    return False


def isSubTree(root1, root2):
    prestr1 = serialByPre(root1)
    prestr2 = serialByPre(root2)
    return getIndexOf(prestr1, prestr2) != -1

def serialByPre(root):
    if not root:
        return '#!'
    res = ""
    stack = [root]
    while stack:
        node = stack.pop()
        res += node.val + '!'
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

def getIndexOf(string, pattern):
    if pattern is None or string is None or len(string) < 1 or len(string) < len(pattern):
        return -1
    p1, p2 = 0, 0
    nexts = getNext(pattern)
    while p1 < len(string) and p2 < len(pattern):
        if string[p1] == string[p2]:
            p1 += 1
            p2 += 1
        elif nexts[p2] == -1:
            p1 += 1
        else:
            p2 = nexts[p2]
    return p1-p2 if p2 == len(pattern) else -1


def getNext(pattern):
    if len(pattern) == 1:
        return [-1]
    nexts = [-1] * len(pattern)
    nexts[1] = 0
    index, cur = 2, 0
    while index < len(pattern):
        if pattern[index-1] == pattern[cur]:
            cur += 1
            nexts[index] = cur
            index += 1
        elif cur > 0:
            cur = nexts[cur]
        else:
            nexts[index] = 0
            index += 1
    return nexts




























