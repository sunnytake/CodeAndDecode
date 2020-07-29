# coding=utf-8
'''
假设链表中每一个节点的值都在0-9之间，那么链表整体就可以代表一个函数
例如：9->3->7，可以代表整数937
给定两个这种链表的头节点head1和head2，请生成代表两个整数相加值得结果链表
例如：链表1为9->3->7，链表2位6->3，最后生成新的结果链表为1->0->0->0
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# 利用栈
def addList1(head1, head2):
    stack1, stack2 = [], []
    while head1:
        stack1.append(head1)
        head1 = head1.next
    while head2:
        stack2.append(head2)
        head2 = head2.next
    node = None
    jinwei, pre = 0, None
    while stack1 or stack2:
        if stack1:
            val1 = stack1.pop().val
        else:
            val1 = 0
        if stack2:
            val2 = stack2.pop().val
        else:
            val2 = 0
        val = val1 + val2 + jinwei
        node = Node(val % 10)
        node.next = pre
        pre = node
        jinwei = val // 10

    if jinwei == 1:
        node = Node(1)
        node.next = pre
    return node

# 利用链表逆序，省掉栈的空间
def addList2(head1, head2):
    head1 = reverseList(head1)
    head2 = reverseList(head2)
    pre, node = None, None
    jinwei = 0
    while head1 or head2:
        if head1:
            val1 = head1.val
            head1 = head1.next
        else:
            val1 = 0
        if head2:
            val2 = head2.val
            head2 = head2.next
        else:
            val2 = 0
        val = val1 + val2 + jinwei
        node = Node(val % 10)
        node.next = pre
        pre = node
        jinwei = val // 10
    if jinwei == 1:
        node = Node(1)
        node.next = pre
    reverseList(head1)
    reverseList(head2)
    return node

def reverseList(head):
    pre, cur = None, head
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre

if __name__ == '__main__':
    node1 = Node(9)
    node2 = Node(3)
    node3 = Node(7)
    node4 = Node(6)
    node5 = Node(3)
    node1.next = node2
    node2.next = node3
    node4.next = node5
    node = addList1(node1, node4)
    while node:
        print(node.val)
        node = node.next









































