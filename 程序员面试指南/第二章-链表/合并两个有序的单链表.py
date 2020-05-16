# coding=utf-8
'''
给定两个有序单链表的头节点head1和head2，请合并两个有序链表，合并后的链表依然有序，并返回合并后链表的头节点
例如：
0 -> 2 -> 3 -> 7 -> null
1 -> 3 -> 5 -> 7 -> 9 -> null
合并后的链表为：0 -> 1 -> 2 -> 3 -> 5 -> 7 -> 7 -> 9 -> null
'''

def merge(head1, head2):
    if not head1 or not head2:
        return head1 if head1 is not None else head2
    head = head1 if head1.val <= head2.val else head2.val
    cur1 = head1 if head == head1 else head2
    cur2 = head2 if head == head1 else head1
    pre = None
    while cur1 and cur2:
        if cur1.val <= cur2.val:
            pre = cur1
            cur1 = cur1.next
        else:
            temp = cur2.next
            pre.next = cur2
            cur2.next = cur1
            cur2 = temp
    pre.next = cur1 if cur1 else cur2
    return head



















