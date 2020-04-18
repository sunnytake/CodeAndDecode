# coding=utf-8

class StackWithQueue:
    data, help = [], []

    def swap(self):
        self.data, self.help = self.help, self.data

    def push(self, num):
        self.data.append(num)

    def peek(self):
        if len(self.data) == 0:
            raise IndexError
        while len(self.data) != 1:
            self.help.append(self.data.pop[0])
        res = self.data.pop(0)
        self.help.append(res)
        self.swap()
        return res

    def pop(self):
        if len(self.data) == 0:
            raise IndexError
        while len(self.data) != 1:
            self.help.append(self.data.pop[0])
        res = self.data.pop(0)
        self.swap()
        return res

