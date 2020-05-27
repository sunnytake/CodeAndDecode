# coding=utf-8

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# 借助辅助数据：时间复杂度为O(N)，空间复杂度为O(N)
def listPartition1(head, pivot):
    if not head:
        return head
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    arrPartition(nodes, pivot)
    pre = nodes[0]
    for node in nodes[1:]:
        pre.next = node
        pre = node
    return nodes[0]

def arrPartition(nodes, pivot):
    less, cur, more = -1, 0, len(nodes)
    while cur != more:
        if nodes[cur].val < pivot:
            less += 1
            swap(nodes, less, cur)
            cur += 1
        elif nodes[cur].val > pivot:
            more -= 1
            swap(nodes, more, cur)
        else:
            cur += 1

def swap(nodes, i, j):
    if i != j:
        nodes[i], nodes[j] = nodes[j], nodes[i]

# 进阶解法：保持稳定性，时间复杂度O(N)，空间复杂度O(1)
# 利用3个临时链表，
def listPartition2(head, pivot):
    small_start, small_end, equal_start, equal_end, big_start, big_end = None, None, None, None, None, None
    res = None
    cur = head
    while cur:
        next = cur.next
        cur.next = None
        if cur.val < pivot:
            if not small_start:
                small_start = cur
            else:
                small_end.next = cur
            small_end = cur
        elif cur.val > pivot:
            if not big_start:
                big_start = cur
            else:
                big_end.next = cur
            big_end = cur
        else:
            if not equal_start:
                equal_start = cur
            else:
                equal_end.next = cur
            equal_end = cur
        cur = next
    if small_end:
        small_end.next = equal_start
        if not equal_end:
            equal_end = small_end
    if equal_end:
        equal_end.next = big_start
    if small_start:
        return small_start
    elif equal_start:
        return equal_start
    else:
        return big_start



if __name__ == '__main__':
    node1 = Node(9)
    node2 = Node(0)
    node3 = Node(4)
    node4 = Node(5)
    node5 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    res = listPartition1(node1, 3)
    while res:
        print(res.val, end='\t')































