# coding=utf-8
'''
给定一个字符串数组strs，在strs中有些位置为null，但在不为null的位置上，其字符串
是按照字典顺序由小到大依次出现的。再给定一个夫妇穿str，请返回str再strs中出现的最左的位置

strs = [None, "a", None, "a", None, "b", None, "c"], str="a"，返回1
strs = [None, "a", None, "a", None, "b", None, "c"], str=None，返回-1
strs = [None, "a", None, "a", None, "b", None, "c"], str="d"，返回-1
'''
def getIndex(strs, str):
    if not strs or str is None:
        return -1
    res = -1
    left, right = 0, len(strs)-1
    while left <= right:
        mid = (left + right) // 2
        if strs[mid] is not None and strs[mid] == str:
            res = mid
            right = mid - 1
        elif str[mid] is not None:
            if strs[mid] < str:
                left = mid+1
            else:
                right = mid-1
        else:
            index = mid-1
            while strs[index] is None and index >= left:
                index -= 1
            # 如果整个左边区都为None 或 左半区最后一个非None字符串小于str
            if index < left or strs[index] < str:
                left = mid + 1
            else:
                if strs[index] == str:
                    res = index
                right = index - 1





















