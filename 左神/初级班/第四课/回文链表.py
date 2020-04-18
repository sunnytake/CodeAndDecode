# coding=utf-8

"""
判断一个链表是否为回文结构
给定一个链表的头节点head，请判断该链表是否为回文机构
例如：
1->2->1，返回true
1->2->2->1，返回true
15->6->15，返回true
1->2->3，返回false
进阶：如果链表长度为N，时间复杂度达到O（N），额外空间复杂度达到O(1)
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def isReverseLink(head):
    if not head.next:
        return True

    p_fast, p_slow = head, head
    # 寻找中间节点
    # 结束时p_low指向中间节点（基数），或者中间节点的前一个节点（偶数）
    while p_fast.next and p_fast.next.next:
        p_fast = p_fast.next.next
        p_slow = p_slow.next

    node = p_slow.next
    p_slow.next = None
    while node:
        print(node.val)
        temp = node.next
        node.next = p_slow
        p_slow = node
        node = temp

    p1, p2 = head, p_slow
    while p1 and p2 and p1.val == p2.val:
        p1 = p1.next
        p2 = p2.next
    if not p1:
        res = True
    else:
        res = False

    # 恢复链表
    p3 = p_slow.next
    while p3:
        temp = p3.next
        p3.next = p_slow
        p_slow = p3
        p3 = temp

    return res

if __name__ == '__main__':
    """
    1->2->1，返回true
1->2->2->1，返回true
15->6->15，返回true
1->2->3，返回false
    """
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    # node4 = Node(1)
    node1.next = node2
    node2.next = node3
    # node3.next = node4
    print(isReverseLink(node1))







