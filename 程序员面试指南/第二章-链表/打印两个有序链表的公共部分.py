# coding=utf-8
'''
给定两个有序链表的头指针head1和head2，打印两个链表的公共部分
'''
class Node:
    def __init__(self, val):
        self.val = val

def printCommonPart(head1, head2):
    res = []
    while head1 and head2:
        if head1.val < head2.val:
            head1 = head1.next
        elif head1.val > head2.val:
            head2 = head2.next
        else:
            res.append(head1.val)
            head1 = head1.next
            head2 = head2.next
    return res

























