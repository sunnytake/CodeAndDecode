# coding=utf-8
'''
给定一个无序单链表的头节点head，实现单链表的选择排序
要求：额外空间复杂度为O(1)
'''

def selectSort(head):
    # 排序部分的头部和尾部
    res_head, res_tail = None, None
    # 未排序部分
    cur = head
    # 最小节点，最小节点的前一个
    small, small_pre = None, None
    while cur:
        small = cur
        small_pre = getSmallestPreNode(cur)
        if small_pre:
            small = small_pre.next
            small_pre.next = small.next
        # 当最小值为cur（即未排序部分的头节点）时，需要将头节点移动到排序部分，cur后移一位
        # 否则cur不变
        cur = cur.next if cur == small else cur
        if not res_head:
            res_head = small
        else:
            res_tail.next = small
        res_tail = small
    return res_head


def getSmallestPreNode(head):
    pre, cur = head, head.next
    small_pre, small = None, head
    while cur:
        if cur.val < small.val:
            small_pre = pre
            small = cur
        pre = cur
        cur = cur.next
    return small_pre
