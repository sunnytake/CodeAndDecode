# coding=utf-8
'''
给定一个单链表的头部节点head，链表长度为N，
如果N为偶数，那么前N/2个节点算作左半区，后N/2个节点算作右半区
如果N为奇数，那么前N/2个节点算作左半区，后N/2+1个节点算作右半区
左半区从左到右依次记为L1 -> L2 -> ...，请将单链表调整成L1 -> R1 -> L2 -> R2 -> ...的形式
例如：
1 -> null，调整为1 -> null
1 -> 2 -> null，调整为1 -> 2 -> null
1 -> 2 -> 3 -> null，调整为1 -> 2 -> 3 -> null
1 -> 2 -> 3 -> 4 -> null，调整为1 -> 3 -> 2 -> 4 -> null
'''
def relocate(head):
    if not head or not head.next:
        return head
    # 左部分最后一个节点
    mid = head
    right = head.next
    while right.next and right.next.next:
        mid = mid.next
        right = right.next.next
    right = mid.next
    mid.next = None
    mergeLR(head, right)

def mergeLR(left, right):
    while left.next:
        right_temp = right.next
        left_temp = left.next
        right.next = left_temp
        left.next = right
        left = left_temp
        right = right_temp
    left.next = right

























