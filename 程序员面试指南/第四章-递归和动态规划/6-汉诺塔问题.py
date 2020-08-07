# coding=utf-8
'''
给定一个整数n，嗲表汉诺塔游戏中从小打到放置的n个圆盘，假设开始时所有的圆盘都放在左边的柱子上，
想按照汉诺塔游戏的要求把所有的圆盘都移动到右边的柱子上，实现函数打印最优移动轨迹
'''
def hanoi(n):
    if n > 0:
        process(n, "left", "mid", "right")

def process(n, form, help, to):
    if n == 1:
        print("move from " + form + " to " + to)
    else:
        process(n-1, form, to, help)
        process(1, form, help, to)
        process(n-1, help, form, to)