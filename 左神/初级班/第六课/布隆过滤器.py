# coding=utf-8

"""
要开多大空间：
m=-(n*lnP)/(ln2)^2
    n: 数据量
    m：bit位数
    P：失误率

hash函数的个数:
k = ln2 * （m/n）向上取整

真实的失误率：
(1-e^(-n*k/m))^k
"""
if __name__ == '__main__':
    # 1000个int，32000个bit位
    array = [0]*1000

    index = 30000
    intIndex = index // 32
    bitIndex = index % 32

    array[intIndex] = (array[intIndex] | (1 << bitIndex))