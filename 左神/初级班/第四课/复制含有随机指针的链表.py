# coding=utf-8

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None

def copyLinkWithRandom(head):
    if not head:
        return None
    # 在每个节点后复制一个节点
    p1 = head
    while p1:
        node = Node(p1.val)
        temp = p1.next
        p1.next = node
        node.next = temp
        p1 = temp

    # 复制random节点
    p2 = head
    while p2:
        p2.next.random = p2.random.next
        p2 = p2.next.next

    # 修改next指针
    p3, res = head, head.next
    while res.next:
        p3.next = res.next
        p3 = res.next
        res.next = p3.next
        res = p3.next
    return res