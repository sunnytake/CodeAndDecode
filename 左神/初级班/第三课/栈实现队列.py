# coding=utf-8

class QueueWithStack:
    push_stack, pop_stack = [], []

    def push(self, num):
        self.push_stack.append(num)

    def poll(self):
        if len(self.push_stack) == 0:
            raise IndexError
        # 一次要倒完
        while len(self.push_stack) > 0:
            self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()

    def peek(self):
        if len(self.push_stack) == 0:
            raise IndexError
        while len(self.push_stack) > 0:
            self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]
