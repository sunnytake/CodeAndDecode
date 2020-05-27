# coding=utf-8
'''
给定一个无序单链表的头节点head，删除其中值重复出现的节点
例如：1->2->3->3->4->4->2->1->1->null，删除值重复的节点之后为1->2->3->4->null
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# 使用hash表，时间复杂度为O(N)，空间复杂度为O(N)
def removeRep1(head):
    if not head:
        return head
    values = [head.val]
    pre = head
    cur = head.next
    while cur:
        if cur.val not in values:
            pre = cur
            values.append(cur.val)
        else:
            pre.next = cur.next
        cur = cur.next
    return head

# 使用类似排序的过程，时间复杂度为O(N^2)，空间复杂度为O(1)
def removeRep(head):
    cur = head
    while cur:
        pre = cur
        next = cur.next
        while next:
            if cur.val != next.val:
                pre = next
            else:
                pre.next = next.next
            next = next.next
        cur = cur.next
    return head



























