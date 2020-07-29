# coding=utf-8
'''
一个环形单链表从头节点head开始不降序，同时由最后的节点指回头节点
给定这样一个环形单链表的头节点head和一个整数num，请生成节点值为num的新节点
并插入到这个环形链表中，保证调整后的链表依然有序
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insertNum(head, num):
    node = Node(num)
    # 如果链表为空，node自己组成环形链表，返回node
    if not head:
        node.next = node
        return node
    # 遍历找到插入位置
    pre, cur = head, head.next
    while cur != head:
        if pre.val <= num <= cur.val:
            break
        pre = cur
        cur = cur.next
    # 插入node
    # 情况1：在cur=head前找到符合条件的插入位置，则将node插入pre和cur中间即可
    pre.next = node
    node.next = cur
    # 情况2：没有找到符合条件的插入位置，此时分为两种情况
    #   情况2.1：num大于原链表中所有元素，则node应该为链表尾部
    #   情况2.2：num小于原链表中所有元素，则node应该为链表头部
    return head if head.val < num else node



























