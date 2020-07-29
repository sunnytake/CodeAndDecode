# coding=utf-8

'''
链表节点值类型为int，给定一个链表中的节点node，但不给定整个链表的头节点，如何在链表中删除node？
要求：时间复杂度为O(1)

思路：例如链表1 -> 2 -> 3 -> null，只知道要删除节点2，而不知道头节点，只需要把节点2的值变成节点3的值，然后在链表中删除节点3即可

存在的问题：
1、无法删除最后一个节点
2、本质上不是删除了node节点，而是把node节点的值改变，然后删除node 的下一个节点，在工程中可能会带来问题。
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def removeNodeWired(node):
    if not node:
        return
    next = node.next
    if not next:
        raise Exception("can not remove last node")
    node.val = next.val
    node.next = next.next