# coding=utf-8

'''
给定一个无序单链表的头节点head，删除其中值重复出现的节点
例如：1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 2 -> 1 -> 1 -> null，删除值重复的节点之后为1 -> 2 -> 3 -> 4 -> null
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# 时间复杂度为O(N^2)，空间复杂度为O(1)
def removeRep(head):
    if not head:
        return head

    cur, pre, next = head, None, None
    while cur:
        pre = cur
        next = cur.next
        while next:
            if cur.val == next.val:
                pre.next = next.next
            else:
                pre = next
            next = next.next
        cur = cur.next

    return head

# 时间复杂度为O(N)，空间复杂度为O(N)
def removeRepWithHash(head):
    if not head:
        return head
    values = []
    pre = head
    cur = head.next
    while cur:
        if cur.val not in values:
            values.append(cur.val)
            pre = cur
        else:
            pre.next = cur.next
        cur = cur.next
    return head

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(3)
    node5 = Node(4)
    node6 = Node(4)
    node7 = Node(2)
    node8 = Node(1)
    node9 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    print("方法1：")
    head = removeRep(node1)
    while head:
        print(head.val, end='\t')
        head = head.next
    print('\n去重法：')
    head = removeRep(node1)
    while head:
        print(head.val, end='\t')
        head = head.next