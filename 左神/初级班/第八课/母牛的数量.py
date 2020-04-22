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
def numofNiu1(n):
    if n < 5:
        return n
    nums = [1, 2, 3, 4]
    for i in range(4, n):
        nums.append(nums[i-1] + nums[i-3])
    return nums[n-1]


def numOfNiu(n):
    res = 0
    def process(niu_map, n):
        '''
        :param niu_map:1年，2年，3年的母牛数量
        :return:
        '''
        global res
        if n == 0:
            return
        else:
            n -= 1
            res += niu_map[3]
            temp = niu_map[3]
            niu_map[3] += niu_map[2]
            niu_map[2] += niu_map[1]
            niu_map[1] = temp
            process(niu_map, n)
    process({3: 1, 2: 0, 1: 0}, n)
    return res

