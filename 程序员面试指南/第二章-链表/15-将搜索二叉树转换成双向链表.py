# coding=utf-8

'''
对二叉树的节点来说，有本身的值域，有指向左孩子和右孩子的两个指针；
对双向链表的节点来说，有本身的值域，有指向上一个节点和下一个节点的指针；
在结构上，两种结构有相似性。
现在有一颗搜索二叉树，请将其转换为一个有序的双向链表
示例树：
          6
    4           7
  2    5            9
1   3           8
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def inOrder(root):
    if not root:
        return []
    stack = []
    nodes = []
    node = root
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop(-1)
            nodes.append(node)
            node = node.right
    return nodes

def convert(root):
    nodes = inOrder(root)
    if not nodes:
        return root

    head = nodes.pop(0)
    pre = head
    pre.left = None

    while nodes:
        cur = nodes.pop(0)
        pre.right = cur
        cur.left = pre
        pre = cur

    pre.right = None
    return head

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node6.left = node4
    node6.right = node7
    node4.left = node2
    node2.right = node5
    node2.left = node1
    node2.right = node3
    node7.right = node9
    node9.left = node8
    head = convert(node6)
    while head:
        print(head.val, end='\t')
        head = head.right













