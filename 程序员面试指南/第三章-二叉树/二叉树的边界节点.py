# coding=utf-8
'''
给定一棵二叉树的头节点head，按照如下两种标准分别实现二叉树边界节点的逆时针打印
标准1：
    1.头节点为边界节点
    2.叶节点为边界节点
    3.如果节点在其所在的层中是最左或最右的，也是边界节点
例如，对于树：
                    1
         2                      3
           4                  5    6
         7   8              9   10
               11        12
             13  14   15  16
按照标准1的打印结果为：1,2,4,7,11,13,14,15,16,12,10,6,3
'''
def printEdge1(root):
    if not root:
        return []
    res = []
    height = getHeight(root, 0)
    # 每一层的最左节点和最右节点
    level_edges = [[None, None]]*height
    setLevelEdges(root, 0, level_edges)
    # 左边界
    for level in level_edges:
        res.append(level[0].val)
    # 既不是左边界，也不是右边界的叶子节点
    res += getLeafNotInEdges(root, 0, level_edges)
    # 右边界，但是注意不能也是左边界
    for level in level_edges:
        if level[0] != level[1]:
            res.append(level[1].val)
    return res

def getHeight(root, height):
    if not root:
        return height
    return max(getHeight(root.left, height+1), getHeight(root.right, height+1))

def setLevelEdges(root, level, level_edges):
    if not root:
        return
    if not level_edges[level][0]:
        level_edges[level][0] = root
    level_edges[level][1] = root
    setLevelEdges(root.left, level+1, level_edges)
    setLevelEdges(root.right, level+1, level_edges)

def getLeafNotInEdges(root, level, level_edges):
    if not root:
        return []
    res = []
    if not root.left and not root.right and root not in level_edges[level]:
        res.append(root.val)
    res += getLeafNotInEdges(root.left, level+1, level_edges)
    res += getLeafNotInEdges(root.right, level+1, level_edges)
    return res


























