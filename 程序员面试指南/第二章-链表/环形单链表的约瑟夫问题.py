# coding=utf-8
'''
m个人围成一个圆圈，由第一个人开始报数，报数为3的人出局，
然后再由下一个人重新报1，报到3的人出局。。。
依次进行下去，直到剩下最后一个人

输入：一个环形单向链表的头节点head和报数的值m
返回：最后生存下来的节点，且这个节点自己组成环形单链表，其他节点都删掉
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# 时间复杂度为(m*n)：m为报数值，n为节点数（每删除一个节点要遍历m次）
def josCirclr(head, m):
    if not head or not head.next or m < 1:
        return head
    last = head
    while last.next != head:
        last = last.next
    count = 0
    while head != last:
        count += 1
        if count == m:
            last.next = head.next
            count = 0
        else:
            last = head
        head = last.next
    return head

def josKill2(head, m):
    if not head or not head.next or m < 1:
        return head
    node = head.next
    length = 1
    while node != head:
        length += 1
        node = node.next
    pos = getLive(length, m)
    while pos != 0:
        head = head.next
    head.next = head
    return head

def getLive(length, m):
    if length == 1:
        return 1
    return (getLive(length-1, m) + m - 1) % length + 1

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node1
    print(josCirclr(node1, 3).val)





























