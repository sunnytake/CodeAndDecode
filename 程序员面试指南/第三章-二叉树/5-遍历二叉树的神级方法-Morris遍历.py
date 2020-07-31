# coding=utf-8
'''
给定一棵二叉树的头节点head，完成二叉树的先序、中序和后序遍历
如果二叉树的节点数为N，要求时间复杂度为O(N)，额外空间复杂度为O(1)

之前的方法空间复杂度都无法做到空间复杂度为O(1)，这是因为遍历二叉树的递归方法实际使用了函数栈，
非递归的方法使用了申请的栈，两者的额外空间都与树的高度相关，所以空间复杂度为O(h)，h为二叉树的高度。

递归和非递归的方法都使用了栈结构，目的是处理完二叉树某个节点后可以回到上层去。
这是因为二叉树的结构中，每个节点都有指向孩子节点的指针，所以从上层到下层容易。
但是没有指向父节点的指针，所以从下层到上层需要用栈结构辅助完成。

Morris遍历的实质就是避免使用栈，而是让下层到上层有指针有指针，具体是通过让底层节点指向null的空闲指针
指回上层的某个节点，从而完成下层到上层的移动。
时间复杂度为O(N)
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def morrisIn(root):
    if not root:
        return []
    res = []
    cur1, cur = root, None
    while cur1:
        cur2 = cur1.left
        if cur2:
            while cur2.right and cur2.right != cur1:
                cur2 = cur2.right
            if not cur2.right:
                cur2.right = cur1
                cur1 = cur1.left
                continue
            else:
                cur2.right = None
        res.append(cur1.val)
        cur1 = cur1.right
    return res


def morrisPre(root):
    if not root:
        return []
    res = []
    cur1, cur2 = root, None
    while cur1:
        cur2 = cur1.left
        if cur2:
            while cur2.right and cur2.right != cur1:
                cur2 = cur2.right
            if not cur2.right:
                cur2.right = cur1
                res.append(cur1.val)
                cur1 = cur1.left
                continue
            else:
                cur2.right = None
        else:
            res.append(cur1.val)
        cur1 = cur1.right
    return res


def morrisPos(root):
    if not root:
        return []
    res = []
    cur1, cur2 = root, None
    while cur1:
        cur2 = cur1.left
        if cur2:
            while cur2.right and cur2.right != cur1:
                cur2 = cur2.right
            if not cur2.right:
                cur2.right = cur1
                cur1 = cur1.left
                continue
            else:
                cur2.right = None
                printEdge(cur1.left, res)
        cur1 = cur1.right
    printEdge(root, res)
    return res

def printEdge(root, res):
    tail = reverseEdge(root)
    cur = tail
    while cur:
        res.append(cur.val)
        cur = cur.right
    reverseEdge(root)

def reverseEdge(from_node):
    pre, next = None, None
    while from_node:
        next = from_node.right
        from_node.right = pre
        pre = from_node
        from_node = next
    return pre


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node4.left = node2
    node4.right = node6
    node2.left = node1
    node2.right = node3
    node6.left = node5
    node6.right = node7
    print(morrisIn(node4))
















