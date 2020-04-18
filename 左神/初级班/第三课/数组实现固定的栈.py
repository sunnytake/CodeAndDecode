# coding=utf-8

class ArrayStack:
    array = [None] * 10
    # 指向下一个放入数据的位置
    index = 0

    def peek(self):
        if self.index == 0:
            return None
        return self.array[self.index-1]

    def push(self, num):
        if self.index == len(self.array):
            raise IndexError
        self.array.append(num)

    def pop(self):
        if self.index == 0:
            raise IndexError
        self.index -= 1
        return self.array[self.index]