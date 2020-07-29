# coding=utf-8

'''
给定一个无序单链表的头节点head和一个整数num，将值为num的节点全部删除
例如：链表为1 -> 2 -> 3 -> 4 -> null, num=3，链表调整后为：1 -> 2 -> 4 -> null
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def removeValue(head, num):
    pre, cur = None, head
    new_head = None
    while cur:
        if cur.val != num:
            if not new_head:
                new_head = cur
            pre = cur
        else:
            if pre:
                pre.next = cur.next
        cur = cur.next
    return new_head

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    res = removeValue(node1, 3)
    while res:
        print(res.val, end='\t')
        res = res.next