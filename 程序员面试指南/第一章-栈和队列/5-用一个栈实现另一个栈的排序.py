# coding=utf-8
'''
一个栈中元素的类型为整型，现在想从该栈从顶到底按从大到小的顺序排序，只许申请一个栈。
除此之外，可以申请新的变量，但不能申请额外的数据结构，如何完成排序？
'''
def sortStackByStack(stack):
    help_stack = []
    while stack:
        val = stack.pop()
        while help_stack and help_stack[-1] < val:
            stack.append(help_stack.pop())
        help_stack.append(val)
    while help_stack:
        stack.append(help_stack.pop())
    return stack

stack = [1, 3, 5, 4, 2]
sortStackByStack(stack)
print(stack)


























