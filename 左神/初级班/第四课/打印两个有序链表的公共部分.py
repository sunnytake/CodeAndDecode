# coding=utf-8

"""
给定两个有序链表的头指针head1和head2，打印两个链表的公共部分
"""

"""
当链表中可能存在值相同时：
1 -> 4 -> 5 -> 5 -> 5
     1 -> 2 -> 5 -> 5
此时数据状况（有序）并不能提供优化思路
"""
def printCommon1(head1, head2):
    p1, p2 = head1, head2
    length1, length2 = 0, 0
    res = []
    while p1:
        length1 += 1
        p1 = p1.next
    while p2:
        length2 += 1
        p2 = p2.next
    p_long = head1 if length1 >= length2 else head2
    p_short = head2 if length1 < length2 else head1

    for i in range(abs(length1 - length2)):
        p_long = p_long.next
    while p_long and p_short and p_long != p_short:
        p_long = p_long.next
        p_short = p_short.next

    while p_long:
        res.append(p_long.val)
        p_long = p_long.next
    return res


"""
当链表中不存在值相同时：
1 -> 3 -> 5 -> 5
     2 -> 4 -> 5
此时数据状况可以提供优化思路
"""
def printCommon2(head1, head2):
    res = []
    if not head1 or not head2:
        return res
    if head1 and head2:
        while head1.val < head2.val and head1.next:
            head1 = head1.next
        while head2.val < head1.val and head2.next:
            head2 = head2.next
        if head1.val == head2.val:
            while head1:
                res.append(head1.val)
                head1 = head1.next
    return res