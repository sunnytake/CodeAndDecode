# coding=utf-8
'''
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"
'''
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        return self.process(n, k)

    def generate(self, n):
        '''生成截乘数组'''
        if n < 2:
            return list(range(n))
        arrays = [0, 1]
        for i in range(2, n):
            arrays.append(arrays[-1] * i)
        return arrays[::-1]

    def process(self, n, k):
        vals = list(range(1, n + 1))
        arrays = self.generate(n)
        res = ""
        for i in range(n - 1):
            num = arrays.pop(0)
            res += str(vals.pop((k-1) // num))
            k = k % num
        res += str(vals[0])
        return res

print(Solution().getPermutation(2, 1))