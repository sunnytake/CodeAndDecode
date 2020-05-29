# coding=utf-8
'''
实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作

亚茹最小栈规则：
* 如果最小栈为空，则num也压入
* 如果不为空，则比较newNum和stackMin的栈顶元素哪个更小
* 如果newNum更小或两者相等，则newNum也压入stackMin
* 如果stackMin中栈顶元素更小，则stackMin不压入任何内容
'''
class MyStack:
    def __init__(self):
        self.data = []
        self.mins = []

    def push(self, val):
        if not self.mins:
            self.mins.append(val)
        elif val <= self.mins[-1]:
            self.mins.append(val)
        self.data.append(val)

    def pop(self, val):
        if not self.data:
            raise Exception("stack is empty")
        val = self.data.pop()
        if val == self.mins[-1]:
            self.mins.pop()
        return val

    def getmin(self):
        if not self.mins:
            raise Exception("stack is empty")
        return self.mins[-1]


















