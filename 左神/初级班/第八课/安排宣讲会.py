# coding=utf-8

"""
一些项目要占用一个会议室宣讲，会议室不能同时容纳两个项目的宣讲。
给你一个项目开始的时间和结束的时间（一个数组，里面是一个个具体的项目）
你来安排宣讲的行程，要求会议室进行的宣讲的场次最多，返回这个最多的宣讲场次

贪心策略1：哪个早开始安排哪个（一个从早8点到晚8点，不行）
贪心策略2：哪个时间短安排哪个（一个中间的宣讲会，刚好卡死了两边的宣讲会，不行）
贪心策略3：哪个早结束
"""
import functools

def comparator(a, b):
    if a[1] >= b[1]:
        return 1
    else:
        return -1

def maxPrograms(times):
    if not times:
        return 0
    times.sort(key=functools.cmp_to_key(comparator))
    res = []
    for start, end in times:
        if not res:
            res.append((start, end))
        elif start >= res[-1][1]:
            res.append((start, end))
    return len(res)

if __name__ == '__main__':
    times = [(1, 10), (3, 7), (2, 8), (1, 3), (2, 5)]
    print(maxPrograms(times))
