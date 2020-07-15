# coding=utf-8

class StackWithMin:
    '''
    没有对最小栈进行优化
    '''
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


class StackWithMin:
    '''
    对最小栈进行优化，空间复杂度降低
    '''
    stack = []
    min_stack = []

    def push(self, num):
        self.stack.append(num)
        # 只有在num小于 等于 最小栈栈顶的元素的时，才进入最小栈
        if not self.min_stack or self.min_stack[-1] >= num:
            self.min_stack.append(num)

    def pop(self):
        val = self.stack.pop()
        # 只有在要弹出的元素 等于 最小栈栈顶元素时，最小栈栈顶元素也同时弹出
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

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
    print(stack.getMin()) # 1
    stack.pop() # 弹出1
    print(stack.getMin()) # 3
    stack.pop() # 弹出7
    print(stack.getMin()) # 3
    stack.pop() # 弹出3
    print(stack.getMin()) # 5
    stack.pop() # 弹出10
    print(stack.getMin()) # 5