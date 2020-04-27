# coding=utf-8
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.right = None

def isSubTree(root1, root2):
    str1 = FirstOrderSeq(root1)
    str2 = FirstOrderSeq(root2)
    nexts = getNexts(str2)
    if len(str1) < len(str2):
        return False
    l1, l2 = 0, 0
    while l1 < len(str1) and l2 < len(str2):
        if str1[l1] == str2[l2]:
            l1 += 1
            l2 += 1
        else:
            if nexts[l2] == -1:
                l1 += 1
            else:
                l2 = nexts[l2]
    return True if l2 == len(str2) else False

def FirstOrderSeq(root):
    if not root:
        return '#_'
    res = ""
    res += str(root.val) + '_'
    res += FirstOrderSeq(root.left)
    res += FirstOrderSeq(root.right)
    return res

def getNexts(pattern):
    if len(pattern) == 1:
        return [-1]
    nexts = [0]*len(pattern)
    nexts[0] = -1
    cur = 0
    index = 2
    while index < len(pattern):
        if pattern[index] == pattern[cur]:
            cur += 1
            nexts[index] = cur
            index += 1
        elif cur > 0:
            cur = nexts[cur]
        else:
            nexts[index] = 0
            index += 1
    return nexts