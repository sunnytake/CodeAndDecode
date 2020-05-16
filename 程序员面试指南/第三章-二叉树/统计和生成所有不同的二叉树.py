# coding=utf-8
'''
给定一个整数N，如果N<1，代表空树结构，否则代表中序遍历的结果为{1,2,3...,N}。
请返回可能的二叉树结构有多少。
例如，N=-1时，代表空树结构，返回1；
N=2时，满足中序遍历为{1,2}的二叉树结构，有如下两种：
1                   2
    2           1
进阶：N的含义不变，假设可能的二叉树结构有M种，请返回M个二叉树的头节点，
每一棵二叉树代表一种可能的结构
'''

def numTrees(n):
    if n < 2:
        return 1
    dp_num = [1]
    # N从1到n+1
    for i in range(1, n+1):
        # 根节点依次为第1个，第2个。。。到第i个，左边依次有j-1个节点，右边有i-j个节点
        for j in range(1, i+1):
            dp_num[i] += dp_num[j-1] * dp_num[i-j]
    return dp_num[n]

class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def generateTrees(n):
    return generate(1, n)

def generate(start, end):
    res = []
    if start > end:
        return None
    for i in range(start, end+1):
        root = Node(i)
        left_subtrees = generate(start, i-1)
        right_subtrees = generate(start, i+1, end)
        for left_tree in left_subtrees:
            for right_tree in right_subtrees:
                root.left = left_tree
                root.right = right_tree
                res.append(cloneTree(root))
    return res

def cloneTree(root):
    if not root:
        return root
    root_copy = Node(root.val)
    root_copy.left = cloneTree(root.left)
    root_copy.right = cloneTree(root.right)
    return root_copy























