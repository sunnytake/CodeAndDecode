# coding=utf-8

class Queue:
    array = [None]*10
    # 队头的位置
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