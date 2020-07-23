# coding=utf-8

"""
一块金条切成两半，需要花费和长度数值一样的铜板
比如长度为20的金条，不管切成如何的两半，都要花费20个铜板
一群人想整分整块金条，怎么分最省铜板？

例如：
给定数组{10， 20， 30}，代表一共三个人，整块金条的长度为10+20+30=60，金条要切分成10，20,30三个部分。
如果，先把长度60的金条切成10和50，花费60，再把长度50的金条切分成20和30，花费50，一共花费110铜板
但是如果，先把长度60的金条分成30和30，花费60，再把长度30金条分成10和20，花费30，一共花费90铜板
输入一个数组，返回分割的最小代价
"""
def splitGold(array):
    '''
    哈夫曼树的思想
    '''
    if len(array) < 2:
        return 0
    stack = MinStack(array)
    res = 0
    while stack.data:
        min1 = stack.pop()
        min2 = stack.pop()
        temp = min1 + min2
        res += temp
        if len(stack.data) >= 1:
            stack.insert(temp)
        else:
            break
    return res

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
        '''
        插入到数组尾部，因此是上浮
        '''
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
        '''
        从上往下调整
        '''
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


if __name__ == '__main__':
    array = [10, 20, 30]
    print(splitGold(array))