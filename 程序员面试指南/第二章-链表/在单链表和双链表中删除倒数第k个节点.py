# coding=utf-8
'''
分别实现两个函数，一个可以删除单链表中倒数第K个节点，另一个可以删除双链表中
倒数第K个节点
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def removeLastKthNode(head, k):
    if not head or k < 1:
        return head
    cur = head
    while cur:
        k -= 1
        cur = cur.next
    if k == 0:
        head = head.next
    if k < 0:
        cur = head
        while k + 1 != 0:
            cur = cur.next
        cur.next = cur.next.next
    return head


class DoubleNode:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None

def removeLastKthNode2(head, k):
    if not head or k < 1:
        return head
    cur = head
    while cur:
        k -= 1
        cur = cur.next
    if k == 0:
        head = head.next
        head.pre = None
    if k < 0:
        cur = head
        while k + 1 != 0:
            cur = cur.next
        next = cur.next.next
        cur.next = next
        if next:
            next.pre = cur
    return head






















