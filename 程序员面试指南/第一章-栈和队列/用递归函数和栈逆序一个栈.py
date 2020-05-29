# coding=utf-8
'''
一个栈依次压入1、2、3、4、5，那么从栈顶到栈底分别为5、4、3、2、1.将这个栈转置后，
从栈顶到栈底为1、2、3、4、5，也就是实现栈中元素的逆序，但是只能用递归函数来实现，
不能用其他数据结构
'''
# 方法1：将栈stack的栈底元素返回并移除
def getAndRemoveLastElement(stack):
    res = stack.pop()
    if not stack:
        return res
    else:
        last = getAndRemoveLastElement(stack)
        stack.append(res)
        return last

# 方法2：逆序一个栈
def reverse(stack):
    if not stack:
        return
    val = getAndRemoveLastElement(stack)
    reverse(stack)
    stack.append(val)
    return stack

















