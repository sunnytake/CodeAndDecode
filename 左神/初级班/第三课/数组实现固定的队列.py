# coding=utf-8

class ArrayQueue:
    array = [None]*10
    # start:弹出元素的位置 end:插入元素的下一个位置
    start, end, size = 0, 0, 0

    def peek(self):
        if self.size == 0:
            return None
        return self.array[self.start]

    def push(self, num):
        if self.size == len(self.array):
            raise IndexError
        self.size += 1
        self.array.append(num)
        self.end = (self.end+1) % len(self.array)

    def pool(self):
        if self.size == 0:
            raise IndexError
        self.size -= 1
        tmp = self.start
        self.start = (self.start+1) % len(self.array)
        return self.array[tmp]