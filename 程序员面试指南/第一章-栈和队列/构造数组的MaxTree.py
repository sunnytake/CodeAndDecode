# coding=utf-8
'''
一个数组的MaxTree定义如下：
* 数组必须没有重复元素
* MaxTree是一棵二叉树，数组的每一个值对应一个二叉树节点
* 包括MaxTree树在内且在其中的每一棵子树上，值最大的节点都是树的头
给定一个没有重复元素的数组arr，写出生成这个数组的MaxTree的函数，
要求如果数组长度为N，则时间复杂度为O(N)，额外空间复杂度为O(N)
'''

'''
建树原则：
* 每一个数的父节点是它左边第一个比它大的数和它右边第一个比它大的数中，较小的那个
* 如果一个数左边没有比它大的数，右边也没有。也就是说，这个数是整个数组的最大值，那么这个数是MaxTree的头节点
'''
def getMaxTree(arr):
    pass






















