# coding=utf-8
'''
给定一个单链表的头节点head，实现一个调整单链表的函数，使得每k个节点之间逆序，
如果最后不够K个节点一组，则不调整最后几个节点
例如：
链表：1->2->3->4->5->6->7->8->null, K=3
调整后为：3->2->1->6->5->4->7->8->null，其中7和8不调整，因为不够一组
'''
# 利用栈结构：时间复杂度为O(N)，空间复杂度为O(N)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverseKNodes1(head, k):
    if k < 2:
        return head
    stack = []
    pre, cur = None, head
    new_head = None
    while cur:
        next = cur.next
        stack.append(cur)
        if len(stack) == k:
            pre = resign1(stack, pre, next)
            if new_head is None:
                new_head = cur
        cur = next
    return new_head

def resign1(stack, left, right):
    while stack:
        node = stack.pop()
        if left:
            left.next = node
        left = node
    left.next = right
    return left

# 直接在原链表进行调整：时间复杂度为O(N)，空间复杂度为O(1)
def reverseKNodes2(head, k):
    if k < 2:
        return head
    pre, cur = None, head
    new_head = None
    count = 1
    while cur:
        next = cur.next
        if count == k:
            start = head if pre is None else pre.next
            if new_head is None:
                new_head = cur
            resign2(start, cur, pre, next)
            pre = start
            count = 0
        count += 1
        cur = next
    return new_head

def resign2(start, end, left, right):
    pre, cur = start, start.next
    while cur != right:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    if left is not None:
        left.next = end
    start.next = right




























