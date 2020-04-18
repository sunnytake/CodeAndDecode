# coding=utf-8

"""
两个单链表相交的一系列问题
在本题中，单链表可能有环，也可能无环。
给定两个单链表的头结点head1和head2，这两个链表可能相交，也可能不想交。
请实现一个函数，如果两个链表相交，请返回相交的第一个节点；
如果不想交，返回null即可。
要求：如果链表1的长度为N，链表2的长度为M，时间复杂度清大道O(N+M)，额外空间复杂度请达到O(1)
"""
def getCirclrEnter(head):
    '''
    判断链表是否有环
    :param head: 链表头指针
    :return: 有环返回环入口，否则返回null
    '''
    # 一个快指针，每次走两步；一个慢指针，每次走一步
    p_fast, p_slow = head, head
    while p_fast != p_slow:
        if not p_fast.next or not p_fast.next.next:
            return None
        p_slow = p_slow.next
        p_fast = p_fast.next.next
    # 快慢指针相交后，快指针从头开始，每次走一步，下次相交即为环入口
    p_fast = head
    while p_fast != p_slow:
        p_fast = p_fast.next
        p_slow = p_slow.next
    return p_fast

def getCrossPoint1(head1, head2):
    '''
    当两个链表都无环时找交点
    :param head1:
    :param head2:
    :return: 如果相交返回第一个相交节点，否则返回None
    '''
    p1, p2 = head1, head2

    length1, length2 = 1, 1
    while p1.next:
        p1 = p1.next
        length1 += 1
    while p2.next:
        p2 = p2.next
        length2 += 1

    # 此时p1,p2为两个链表的尾结点，通过尾节点是否相同判断是否相交
    # 不相同，则不想交
    if p1 != p2:
        return None

    p_long = head1 if length1 >= length2 else head2
    p_short = head2 if length1 >= length2 else head1
    for i in range(abs(length2 - length1)):
        p_long = p_long.next

    while p_long != p_short:
        p_long = p_long.next
        p_short = p_short.next
    return p_long

def getCrossPoint2(head1, head2, p_circlr):
    '''
    获取两个同一环入口的第一个相交节点
    :param head1:
    :param head2:
    :param p_circlr:
    :return:
    '''
    # 以入环节点作为尾节点即可，其它和无环链表相同
    p1, p2 = head1, head2
    length1, length2 = 1, 1
    while p1 != p_circlr:
        p1 = p1.next
        length1 += 1
    while p2 != p_circlr:
        p2 = p2.next
        length2 += 1
    p_long = head1 if length1 >= length2 else head2
    p_short = head2 if length1 >= length2 else head1
    for i in range(abs(length1-length2)):
        p_long = p_long.next
    while p_long != p_short:
        p_long = p_long.next
        p_short = p_short.next
    return p_long


def getCrossPoint(head1, head2):
    if not head1 or not head2:
        return None

    # 1. 判断是否有环
    p_circlr1 = getCirclrEnter(head1)
    p_circlr2 = getCirclrEnter(head2)

    # 2. 如果都没有环
    if not p_circlr1 and not p_circlr2:
        return getCrossPoint1(head1, head2)
    # 3. 如果都有环
    elif p_circlr1 and p_circlr2:
        # 3.1 入环节点相同
        if p_circlr1 == p_circlr2:
            return getCrossPoint2(head1, head2, p_circlr1)
        # 3.2 入环节点不同
        else:
            # 判断是否为同一个环，若不是，返回空，若是则两个链表在环上相交，随便返回一个即可
            p_temp = p_circlr1.next
            while p_temp != p_circlr1:
                # 两个链表有同一个环,返回环上任意节点即可
                if p_temp == p_circlr2:
                    return p_circlr2
                p_temp = p_temp.next
            return None
    # 一个有环一个没环，肯定不想交
    return None
