# coding=utf-8

class QueueWithStack:
    '''
    入队时：元素直接放入push_stack中
    出队时：如果pop_stack非空，直接出；否则把push_stack的所有元素压入pop_stack，然后再出。
    '''
    push_stack, pop_stack = [], []

    def push(self, num):
        self.push_stack.append(num)

    def poll(self):
        if len(self.push_stack) + len(self.pop_stack) == 0:
            raise IndexError
        if not self.pop_stack:
            while len(self.push_stack) > 0:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()

    def peek(self):
        if len(self.push_stack) + len(self.pop_stack) == 0:
            raise IndexError
        if not self.pop_stack:
            while len(self.push_stack) > 0:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]

if __name__ == '__main__':
    queue = QueueWithStack()
    queue.push(1)
    queue.push(2)
    print(queue.poll())
    queue.push(3)
    print(queue.poll())