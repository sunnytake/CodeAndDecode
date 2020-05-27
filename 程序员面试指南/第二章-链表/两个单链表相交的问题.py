# coding=utf-8
'''
给定两个单链表头节点head1和head2
单链表可能有环，也可能无环
两个链表可能相交，也可能不想交
请实现一个函数，如果两个链表相交，返回相交的第一个节点；如果不想交，返回null
'''

'''
链表是否有环？返回第一个入环节点
1. 设置一个慢指针slow和一个快指针fast。在开始时，slow和fast都指向链表的头节点head。
然后slow每次移动一步，fast每次移动两步，在链表中遍历
2.如果链表无环，那么fast一定先到终点，一旦fast到达终点，说明链表无环，直接返回null
3.如果链表有环，那么fast和slow一定会在环中的某个位置相遇，当相遇时：
    fast回到head，slow不动，接下来fast和slow每次都移动一步，继续遍历
    fast和slow一定会再次相遇，并且相遇节点为环入口节点
'''
def getLoopNode(head):
    if not head or not head.next or not head.next.next:
        return None
    p1, p2 = head.next, head.next.next
    while p1 != p2:
        if not p2.next or not p2.next.next:
            return None
        p2 = p2.next.next
        p1 = p1.next

    p2 = head
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1

# 无环链表是否相交？返回第一个相交节点
def noLoop(head1, head2):
    if not head1 or not head2:
        return None
    p1, p2 = head1, head2
    length1, length2 = 0, 0
    while p1:
        p1 = p1.next
        length1 += 1
    while p2:
        p2 = p2.next
        length2 += 1
    if length1 >= length2:
        long, short = head1, head2
    else:
        long, short = head2, head1
    diff = abs(length1-length2)
    while diff != 0:
        diff -= 1
        long = long.next
    while long != short:
        long = long.next
        short = short.next
    return short

# 有环链表是否相交？返回第一个相交节点
def bothLoop(head1, loop1, head2, loop2):
    if loop1 != loop2:
        # 判断是否在入环之前相交
        node1, node2 = head1, head2
        length1, length2 = 0, 0
        while node1:
            length1 += 1
            node1 = node1.next
        while node2:
            length2 += 1
            node2 = node2.next
        if length1 >= length2:
            long, short = node1, node2
        else:
            long, short = node2, node1
        diff = abs(length1 - length2)
        while diff != 0:
            diff -= 1
            long = long.next
        while long != short:
            long = long.next
            short = short.next
        return long
    else:
        node1 = loop1.next
        while node1 != loop1:
            if node1 == loop2:
                return node1
            node1 = node1.next
        return None

# 主方法
def getIntersectNode(head1, head2):
    if not head1 or not head2:
        return None
    loop1 = getLoopNode(head1)
    loop2 = getLoopNode(head2)
    if not loop1 and not loop2:
        return noLoop(head1, head2)
    if loop1 and loop2:
        return bothLoop(head1, loop1, head2, loop2)
    return None







































