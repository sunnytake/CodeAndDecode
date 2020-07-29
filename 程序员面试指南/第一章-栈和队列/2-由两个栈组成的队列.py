# coding=utf-8
'''
编写一个类，用两个栈实现队列，支持队列的基本操作（add、poll、peek）
'''
class QueueWithStack:
    def __init__(self):
        self.push = []
        self.pop = []

    def add(self, val):
        self.push.append(val)

    def poll(self):
        if not self.push and not self.pop:
            raise Exception("Queue if empty!")
        elif not self.pop:
            while self.push:
                self.pop.append(self.push.pop())
        return self.pop.pop()

    def peek(self):
        if not self.push and not self.pop:
            raise Exception("Queue if empty!")
        elif not self.pop:
            while self.push:
                self.pop.append(self.push.pop())
        return self.pop[-1]




















