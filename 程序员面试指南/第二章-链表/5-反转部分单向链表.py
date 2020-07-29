# coding=utf-8
'''
给定一个单向链表的头节点head，以及两个整数from和to，在单向链表上把第from
个节点到第to个节点这一部分进行反转

例如：
1->2->3->4->5->null，from=2, to=4
调整结果为：1->4->3->2->5->null
1->2->3->null, from=1, to=3
调整结果为：3->2->1->null
'''
def reversePart(head, from_num, to_num):
    from_node_pre, to_node_next = None, None
    length = 0
    node = head
    while node:
        length += 1
        if length == from_num - 1:
            from_node_pre = node
        if length == to_num + 1:
            to_node_next = node
        node = node.next
    if from_num > to_num or from_num < 1 or to_num > length:
        return head

    if from_node_pre is None:
        start = head
    else:
        start = from_node_pre.next
    next = start.next
    start.next = to_node_next
    while next != to_node_next:
        temp = next.next
        next.next = start
        start, next = next, temp
    if from_node_pre:
        from_node_pre.next = start
        return head
    return start






















