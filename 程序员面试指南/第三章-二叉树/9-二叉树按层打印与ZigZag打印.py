# coding=utf-8
'''
给定一棵二叉树的头节点head，分别实现按层打印和ZigZag打印二叉树的函数
例如，二叉树如下:
            1
        2       3
    4        5     6
           7   8
按层打印时，输出结果如下：
1
2 3
4 5 6
7 8

ZigZag打印时，输出格式必须如下：
1
3 2
4 5 6
8 7
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def printByLevel(root):
    if not root:
        return []
    queue = [root]
    res = []
    while queue:
        help = []
        temp_res = []
        while queue:
            node = queue.pop(0)
            temp_res.append(node.val)
            if node.left:
                help.append(node.left)
            if node.right:
                help.append(node.right)
        res.append(temp_res)
        queue = help
    return res

def printByZigZag(root):
    if not root:
        return []
    queue = [root]
    res = []
    flag = True
    while queue:
        help = []
        temp_res = []
        while queue:
            node = queue.pop(0)
            temp_res.append(node.val)
            if node.left:
                help.append(node.left)
            if node.right:
                help.append(node.right)
        if flag:
            res.append(temp_res)
        else:
            res.append(temp_res[::-1])
        flag = not flag
        queue = help
    return res


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.left = node5
    node3.right = node6
    node5.left = node7
    node5.right = node8
    print(printByLevel(node1))
    print(printByZigZag(node1))






















