# coding=utf-8
# 反转单向链表
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverseList(head):
    pre = None
    while head:
        next = head.next
        head.next = pre
        pre, head = head, next
    return pre

# 反转双向链表
class DoubleNode:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None

def reverseDoubleList(head):
    pre = None
    while head:
        next = head.next
        head.next = pre
        head.pre = next
        pre, head = head, next
    return pre
















