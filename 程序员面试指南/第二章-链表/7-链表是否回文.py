# coding=utf-8
'''
给定一个链表的头节点head，请判断该链表是否为回文结构
例如：
1->2->1，返回True
1->2->2->1，返回True
15->6->15，返回True
1->2->3，返回False
'''
class Node:
    def __init__(self, val):
        self.val = val

# 利用栈，放进去整个链表：时间复杂度O(N)，空间复杂度O(N)
def isPalindrome1(head):
    stack = []
    cur = head
    while cur:
        stack.append(cur)
        cur = cur.val
    cur = head
    while cur:
        if cur.val != stack.pop().val:
            return False
        cur = cur.next
    return True

# 利用栈，放进去一半链表：时间复杂度O(N)，空间复杂度O(N)
def isPalindrome2(head):
    if not head or not head.next:
        return True
    cur, right = head, head.next
    while cur.next and cur.next.next:
        right = right.next
        cur = cur.next.next
    stack = []
    while right:
        stack.append(right)
        right = right.next
    cur = head
    while stack:
        if cur.val != stack.pop().val:
            return False
    return True

# 修改链表后半部分
def isPalindrome3(head):
    if not head or not head.next:
        return True
    p1, p2 = head, head
    # 查找中间节点（靠左）
    while p2.next and p2.next.next:
        p1 = p1.next
        p2 = p2.next.next
    # 翻转右半部分
    right = p1.next
    # 为了后面复原链表
    p1.next = None
    while right:
        temp = right.next
        right.next = p1
        p1 = right
        right = temp
    left, right = head, p1
    while left and right:
        if left.val != right.val:
            res = False
            break
        left = left.next
        right = right.next
    node = p1.next
    p1.next = None
    while p1:
        temp = node.next
        node.next = p1
        p1 = node
        node = temp
    return






























