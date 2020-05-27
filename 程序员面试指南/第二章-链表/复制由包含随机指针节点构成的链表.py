# coding=utf-8
class Node:
    def __init__(self, val):
        self.val = val
        self.next, self.random = None, None

def copyListWithRandom(head):
    if not head:
        return None
    cur = head
    # 复制节点
    while cur:
        next = cur.next
        node = Node(cur.val)
        cur.next = node
        node.next = next
        cur = next
    cur = head
    # 复制随机指针
    while cur:
        node = cur.next
        next = node.next
        node.random = cur.random.next if cur.random else None
        cur = next
    res = head.next
    cur = head
    # 断链
    while cur:
        node = cur.next
        next = node.next
        cur.next = next
        node.next = next.next if next else None
    return res





























