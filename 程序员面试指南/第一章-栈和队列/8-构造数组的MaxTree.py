# coding=utf-8
'''
一个数组的MaxTree定义如下：
* 数组必须没有重复元素
* MaxTree是一棵二叉树，数组的每一个值对应一个二叉树节点
* 包括MaxTree树在内且在其中的每一棵子树上，值最大的节点都是树的头
给定一个没有重复元素的数组arr，写出生成这个数组的MaxTree的函数，
要求如果数组长度为N，则时间复杂度为O(N)，额外空间复杂度为O(N)
'''

'''
建树原则：
* 每一个数的父节点是它左边第一个比它大的数和它右边第一个比它大的数中，较小的那个
* 如果一个数左边没有比它大的数，右边也没有。也就是说，这个数是整个数组的最大值，那么这个数是MaxTree的头节点
例如array = [3, 4, 5, 1, 2]
3的左边第一个比3大的数：无      3的右边第一个比3大的数：4
4的左边第一个比4大的数：无      4的右边第一个比4大的数：5
5的左边第一个比5大的数：无      5的右边第一个比5大的数：无
1的左边第一个比1大的数：5      1的右边第一个比1大的数：2
2的左边第一个比2大的数：5      2的右边第一个比2大的数：无
构成的MaxTree如下：
        5
    4       2
  3       1
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def getMaxTree(array):
    nodes = [Node(val) for val in array]
    left_first_big = leftFirstBiggerNode(array)
    right_first_big = leftFirstBiggerNode(array[::-1])[::-1]
    root = None
    for index, node in enumerate(nodes):
        left, right = left_first_big[index], right_first_big[index]
        if not left and not right:
            root = node
        elif not left:
            if not right.left:
                right.left = node
            else:
                right.right = node
        elif not right:
            if not left.left:
                left.left = node
            else:
                left.right = node
        else:
            parent = left if left.val < right.val else right
            if not parent.left:
                parent.left = node
            else:
                parent.right = node
    return root


def leftFirstBiggerNode(array):
    res = []
    stack = []
    for node in array:
        while stack and stack[-1].val < node.val:
            stack.pop()
        if not stack:
            res.append(None)
        else:
            res.append(stack[-1])
        stack.append(node)
    return res


def leftFirstBigger(array):
    res = []
    stack = []
    for val in array:
        while stack and stack[-1] < val:
            stack.pop()
        if not stack:
            res.append(None)
        else:
            res.append(stack[-1])
        stack.append(val)
    return res

if __name__ == '__main__':
    array = [3, 4, 5, 1, 2]
    print(leftFirstBigger(array))
    print(leftFirstBigger(array[::-1]))
