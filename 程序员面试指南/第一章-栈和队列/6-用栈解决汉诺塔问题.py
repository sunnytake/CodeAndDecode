# coding=utf-8
'''
汉诺塔问题比较经典，这里修改一下游戏规则：
限制不能从最左侧的塔直接移动到最右侧，也不能从最右侧直接移动到最左侧，而是必须经过中间
求当塔有N层的时候，打印最优移动过程和最优移动总步数。
例如，当塔数为2层时，最上层的塔记为1，最下层的塔记为2，则打印：
Move 1 from left to mid
Move 1 from mid to right
Move 2 from left to mid
Move 1 from right to mid
Move 1 from mid to left
Move 2 from mid to right
Move 1 from left to mid
Move 1 from mid to right
'''
# 递归方法
def hanoiProblem1(num, left, mid, right):
    if num < 1:
        return 0
    return process(num, left, mid, right, left, right)

def process(num, left, mid, right, frm, to):
    if num == 1:
        if frm == mid or to == mid:
            print("Move 1 from " + frm + " to " + to)
            return 1
        else:
            print("Move 1 from " + frm + " to " + mid)
            print("Move 1 from " + mid + " to " + to)
            return 2
    if frm == mid or to == mid:
        if frm == left or to == left:
            another = right
        else:
            another = left
        part1 = process(num-1, left, mid, right, frm, another)
        part2 = 1
        print("Move " + num + " from " + frm + " to " + to)
        part3 = process(num-1, left, mid, right, another, to)
        return part1 + part2 + part3
    else:
        part1 = process(num-1, left, mid, right, frm, to)
        part2 = 1
        print("Move " + num + " from " + frm + " to " + mid)
        part3 = process(num-1, left, mid, right, to, frm)
        part4 = 1
        print("Move " + num + " from " + mid + " to " + to)
        part5 = process(num-1, left, mid, right, frm, to)
        return part1 + part2 + part3 + part4 + part5





















