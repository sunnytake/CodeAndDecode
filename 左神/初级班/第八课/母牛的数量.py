# coding=utf-8

"""
母牛每年生一只母牛，新出生的母牛生长三年后也能每年生一只母牛
假设不会死，求N年后，母牛的数量
"""

'''
左神：f(n) = f(n-1) + f(n-3)
f(n)：今年的牛
f(n-1)：去年的牛
f(n-3)：3年前生的牛
'''


def getCows(n):
    if n < 5:
        return n
    nums = [1, 2, 3, 4]
    for i in range(4, n):
        nums.append(nums[i - 1] + nums[i - 3])
    return nums[n - 1]


def getCows2(years):
    # 初始化：0年（刚出生）、1年、2年的母牛都为0头，3年的母牛为1头
    cows = {0: 0, 1: 0, 2: 0, 3: 1}
    for i in range(1, years):
        cows[3] += cows[2]
        cows[2] = cows[1]
        cows[1] = cows[0]
        cows[0] = cows[3]
    return cows[0] + cows[1] + cows[2] + cows[3]

if __name__ == '__main__':
    print(getCows(1), getCows2(1))
    print(getCows(2), getCows2(2))
    print(getCows(3), getCows2(3))
    print(getCows(4), getCows2(4))
    print(getCows(5), getCows2(5))