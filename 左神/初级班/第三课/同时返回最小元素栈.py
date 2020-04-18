# coding=utf-8

class StackWithMin:
    stack = []
    min_stack = []

    def push(self, num):
        if not self.stack:
            self.min_stack.append(num)
        else:
            min_val = self.min_stack[-1]
            self.min_stack.append(num if num < min_val else min_val)
        self.stack.append(num)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None

if __name__ == '__main__':
    stack = StackWithMin()
    stack.push(5)
    stack.push(10)
    stack.push(3)
    stack.push(7)
    stack.push(1)
    print(stack.getMin())
    stack.pop()
    print(stack.getMin())