# coding=utf-8

def maxProfits(money, costs, profits, k):
    '''
    :param money: 起始金额
    :param costs: 每个项目的成本花费
    :param profits: 每个项目的利润
    :param k: 最大可做项目个数
    :return: 做k个项目后的最大金钱
    '''
    for cost, profit in zip(costs, profits):
        pass



def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

class MinStack:
    def __init__(self, array):
        self.data = []
        for val in array:
            self.insert(val)

    def insert(self, val):
        self.data.append(val)
        index = len(self.data) - 1
        parent = (index - 1) // 2
        while parent >= 0 and self.data[index] < self.data[parent]:
                swap(self.data, index, parent)
                index = parent
                parent = (index - 1) // 2

    def pop(self):
        swap(self.data, 0, len(self.data)-1)
        res = self.data.pop(-1)
        self.heapify()
        return res

    def heapify(self):
        index = 0
        left = 2*0 + 1
        while left < len(self.data):
            smallest = left+1 if left+1 < len(self.data) and self.data[left+1] < self.data[left] else left
            smallest = smallest if self.data[index] > self.data[smallest] else index
            if smallest == index:
                break
            swap(self.data, smallest, index)
            index = smallest
            left = 2*index + 1

class MaxStack:
    def __init__(self, array):
        self.data = []
        for val in array:
            self.insert(val)

    def insert(self, val):
        self.data.append(val)
        index = len(self.data) - 1
        parent = (index - 1) // 2
        while parent >= 0 and self.data[index] > self.data[parent]:
                swap(self.data, index, parent)
                index = parent
                parent = (index - 1) // 2

    def pop(self):
        swap(self.data, 0, len(self.data)-1)
        res = self.data.pop(-1)
        self.heapify()
        return res

    def heapify(self):
        index = 0
        left = 2*0 + 1
        while left < len(self.data):
            largest = left+1 if left+1 < len(self.data) and self.data[left+1] > self.data[left] else left
            largest = largest if self.data[index] < self.data[largest] else index
            if largest == index:
                break
            swap(self.data, largest, index)
            index = largest
            left = 2*index + 1

