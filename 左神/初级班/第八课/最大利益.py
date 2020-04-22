# coding=utf-8

class Node:
    def __init__(self, cost, profit):
        self.cost = cost
        self.profit = profit

def maxProfits(money, costs, profits, k):
    '''
    :param money: 起始金额
    :param costs: 每个项目的成本花费
    :param profits: 每个项目的利润
    :param k: 最大可做项目个数
    :return: 做k个项目后的最大金钱
    '''
    nodes = []
    for cost, profit in zip(costs, profits):
        node = Node(cost, profit)
        nodes.append(node)
    min_stack = MinStack(nodes)
    max_stack = MaxStack(None)
    for i in range(k):
        while min_stack and min_stack.data[0].cost <= money:
            max_stack.insert(min_stack.pop())
            if not max_stack:
                return money
            money += max_stack.pop()[1]
    return money


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

# 按照cost排序
class MinStack:
    def __init__(self, node_array):
        self.data = []
        for node in node_array:
            self.insert(node)

    def insert(self, node):
        self.data.append(node)
        index = len(self.data) - 1
        parent = (index - 1) // 2
        while parent >= 0 and self.data[index].cost < self.data[parent].cost:
                swap(self.data, index, parent)
                index = parent
                parent = (index - 1) // 2

    def pop(self):
        swap(self.data, 0, len(self.data)-1)
        node = self.data.pop(-1)
        self.heapify()
        return node

    def heapify(self):
        index = 0
        left = 2*0 + 1
        while left < len(self.data):
            smallest = left+1 if left+1 < len(self.data) and self.data[left+1].cost < self.data[left].cost else left
            smallest = smallest if self.data[index].cost > self.data[smallest].cost else index
            if smallest == index:
                break
            swap(self.data, smallest, index)
            index = smallest
            left = 2*index + 1

class MaxStack:
    def __init__(self, node_array):
        self.data = []
        if node_array:
            for node in node_array:
                self.insert(node)

    def insert(self, node):
        self.data.append(node)
        index = len(self.data) - 1
        parent = (index - 1) // 2
        while parent >= 0 and self.data[index].profit > self.data[parent].profit:
                swap(self.data, index, parent)
                index = parent
                parent = (index - 1) // 2

    def pop(self):
        swap(self.data, 0, len(self.data)-1)
        node = self.data.pop(-1)
        self.heapify()
        return node

    def heapify(self):
        index = 0
        left = 2*0 + 1
        while left < len(self.data):
            largest = left+1 if left+1 < len(self.data) and self.data[left+1].profit > self.data[left].profit else left
            largest = largest if self.data[index].profit < self.data[largest].profit else index
            if largest == index:
                break
            swap(self.data, largest, index)
            index = largest
            left = 2*index + 1

