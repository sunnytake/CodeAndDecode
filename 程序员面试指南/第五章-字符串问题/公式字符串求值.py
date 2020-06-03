# coding=utf-8
'''
给定一个字符串str，str表示一个公式，公式里可能有整数、加减乘除符号和左右括号，
返回公式的计算结果

str="48*((70-65)-43)+8*1"，返回-1816
str="3+1*4"，返回7
str="3+(1*4)"，返回7
'''
def getValue(str):
    if not str:
        return 0

    splits = strSplit(str)
    stack = []
    for split in splits:
        if split == ')':
            val2 = stack.pop()
            op = stack.pop()
            val1 = stack.pop()
            if stack[-1] == '(':
                stack.pop()
            stack.append(operate(val1, val2, op))
        else:
            stack.append(split)
    print(stack)
    # 算乘除
    help_stack = []
    while stack and len(stack) >= 3:
        val2 = stack.pop()
        op = stack.pop()
        if op == '*' or op == '/':
            val1 = stack.pop()
            stack.append(operate(val1, val2, op))
        else:
            help_stack.append(val2)
            help_stack.append(op)
    while stack:
        help_stack.append(stack.pop())

    res = help_stack.pop()
    while help_stack:
        op = help_stack.pop()
        val = help_stack.pop()
        res = operate(res, val, op)
    return res



def operate(val1, val2, op):
    if op == '+':
        return val1 + val2
    elif op == '-':
        return val1 - val2
    elif op == '*':
        return val1 * val2
    else:
        return val1 / val2

def strSplit(str):
    splits = []
    index = 0
    while index < len(str):
        if str[index] >= '0' and str[index] <= '9':
            temp = str[index]
            while index+1 < len(str) and str[index+1] >= '0' and str[index+1] <= '9':
                index += 1
                temp += str[index]
            splits.append(int(temp))
        else:
            splits.append(str[index])
        index += 1
    return splits

if __name__ == '__main__':
    str = "3+(1*4)"
    print(getValue(str))


















