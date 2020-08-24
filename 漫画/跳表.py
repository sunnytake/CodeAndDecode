# coding=utf-8

'''
如何解决链表的查找问题
链接：https://mp.weixin.qq.com/s/Ok0laJMn4_OzL-LxPTHawQ
'''
import random


class Node:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None
        self.down = None
        self.up = None

class SkipList:
    # 节点 晋升 的概率
    PROMOTE_RATE = 0.5
    head, tail = None, None
    max_level = 0

    def __init__(self):
        head = Node(-99999)
        tail = Node(99999)
        head.next = tail
        tail.pre = head

    def search(self, data):
        pre = self.findPreNode(data)
        if pre.data == data:
            # 找到节点
            return pre
        else:
            # 未找到节点
            return None

    # 查找值对应的前置节点/值对应的节点
    def findPreNode(self, data):
        node = self.head
        while True:
            while node.next.val != 99999 and node.next.val <= data:
                node = node.next
            if not node.down:
                break
            node = node.down
        return node

    # 插入节点
    def insert(self, data):
        pre = self.findPreNode(data)
        # 如果data相同，直接返回
        if pre.val == data:
            return
        node = Node(data)
        self.appendNode(pre, node)
        current_level = 0
        # 随机决定节点是否 晋升
        rand = random.random()
        while rand < self.PROMOTE_RATE:
            # 如果当前层已经是最高层，需要增加一层
            if current_level == self.max_level:
                self.addLevel()
            # 找到上一层的前置节点
            while not pre.up:
                pre = pre.pre
            pre = pre.up
            # 把 晋升 的新节点插入到上一层
            upper_Node = Node(data)
            self.appendNode(pre, upper_Node)
            upper_Node.down = node
            node.up = upper_Node
            node = upper_Node
            current_level += 1

    # 在前置节点后面添加新节点
    def appendNode(self, preNode, newNode):
        newNode.pre = preNode
        newNode.next = preNode.next
        preNode.next.pre = newNode
        preNode.next = newNode

    # 增加一层
    def addLevel(self):
        self.max_level += 1
        p1 = Node(-99999)
        p2 = Node(99999)
        p1.next = p2
        p2.pre = p1
        p1.down = self.head
        self.head.up = p1
        p2.down = self.tail
        self.tail.up = p2
        self.head = p1
        self.tail = p2

    # 删除节点
    def remove(self, data):
        removed_node = self.search(data)
        if not removed_node:
            return False
        current_level = 0
        while removed_node:
            removed_node.next.pre = removed_node.pre
            removed_node.pre.next = removed_node.next
            # 如果不是最底层，且只有无穷小和无穷大节点，删除该层
            if current_level != 0 and removed_node.pre.val == -99999 and removed_node.next.val == 99999:
                self.removeLevel(removed_node.pre)
            else:
                self.max_level += 1
            removed_node = removed_node.up
        return True

    # 删除一层
    def removeLevel(self, node):
        right_node = node.next
        # 如果删除层是最高层
        if not node.up:
            node.down.up = None
            right_node.down.up = None
        else:
            node.up.down = node.down
            node.down.up = node.up
            right_node.up.down = right_node.down
            right_node.down.up = right_node.up
        self.max_level -= 1

    # 输出底层链表
    def printList(self):
        node = self.head
        while node.down:
            node = node.down
        while node.next.data != 99999:
            print(node.next.val, end="\t")
            node = node.next
        print("\n")