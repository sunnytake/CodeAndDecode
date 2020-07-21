# coding=utf-8

"""
将单向链表按某值划分成左边小、中间相等、右边大的形式：
给定一个单向链表的头结点head，节点的值类型是整型，再给定一个整数pivot。
实现一个调整链表的函数，将链表调整为左部分都是值小于pivot的节点，中间部分都是值等于pivot的节点，右部分都是值大于pivot的节点
除这个要求外，对调整后的节点顺序没有更多的要求。
例如：
链表9 -> 0 -> 4 ->5 -> 1, pivot=3
调整后链表可以是1 -> 0 -> 4 -> 9 -> 5,也可以是0 -> 1 -> 9 -> 5 -> 4
总之，满足左部分都是小于3的节点，中间部分都是等于3的节点（本例中这个部分为空），右部分都是大于3的节点即可。
对某部分内部的节点顺序不作要求

进阶：在原问题的要求之上再增加如下两个要求：
1). 在左、中、右三个部分的内部也做稳定性要求，要求每部分里的节点从左到右的顺序与原链表中节点的先后次序一致（稳定性）
例如：
链表9 -> 0 > 4 -> 5 -> 1, pivot=3
调整后的链表是0 -> 1 -> 9 -> 4 -> 5
在满足原问题要求的同时，左部分节点从左到右为0、1。在原链表中也是先出现0，后出现1；
中间部分在本例中为空，不再讨论；
右部分节点从左到右为9、4、5.在原链表中也是先出现9，然后出现4，最后出现5
2). 如果链表长度为N，时间复杂度请达到O(N)，额外空间复杂度请达到O(1)
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def LinkILand(head, num):
    if not head:
        return None

    less_head, equal_head, more_head = None, None, None
    less, equal, more = None, None, None
    cur = head
    while cur:
        next = cur.next
        if cur.val < num:
            if not less:
                less_head = cur
                less = cur
            else:
                less.next = cur
                less = less.next
            less.next = None
        elif cur.val > num:
            if not more:
                more_head = cur
                more = cur
            else:
                more.next = cur
                more = more.next
            more.next = None
        else:
            if not equal:
                equal_head = cur
                equal = cur
            else:
                equal.next = cur
                equal = equal.next
            equal.next = None
        cur = next

    # 确定结果的头节点
    if less_head:
        res = less_head
    elif equal:
        res = equal_head
    else:
        res = more_head

    # 如果头节点位于小于部分
    if res == less_head:
        # 连接上等于部分
        if equal_head:
            less.next = equal_head
            # 连接上大于部分
            if more_head:
                equal.next = more_head
        # 直接连上大于部分
        else:
            less.next = more_head
    elif res == equal_head:
        equal.next = more_head
    return res

if __name__ == '__main__':
    node9 = ListNode(9)
    node0 = ListNode(0)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1 = ListNode(1)
    node9.next = node0
    node0.next = node4
    node4.next = node5
    node5.next = node1
    res = LinkILand(node9, 3)
    while res:
        print(res.val, end='\t')
        res = res.next