# coding=utf-8
'''
给定一个字符串数组strs，再给定两个字符串str1和str2，返回strs中str1与str2的最小距离，
如果str1或str2为null，或不在strs中，返回-1

strs=["1", "3", "3", "3", "2", "3", "1"], str1="1", str2="2"，返回2
strs=["CD"], str1="CD", str2="AB"，返回-1
'''
def minDistance(strs, str1, str2):
    if not str1 or not str:
        return -1
    if str1 == str2:
        return 0
    last1, last2 = -1, -1
    min_dis = len(strs)
    for i in range(len(strs)):
        if strs[i] == str1:
            new_dis = i - last2 if last2 != -1 else len(strs)
            min_dis = min(min_dis, new_dis)
            last1 = i
        if strs[i] == str2:
            new_dis = i - last1 if last1 != -1 else len(strs)
            min_dis = min(min_dis, new_dis)
            last2 = i
    return min_dis if min_dis != len(strs) else -1

'''
进阶：如果查询发生的次数有很多，如何把每次查询的时间复杂度降为O(1)
对于数组生成一种记录，记录每个值到其它值得最小距离
生成记录的时间复杂度为O(N^2)，记录的空间复杂度为O(N^2)
生成记录后单次查询的时间复杂度降为O(1)
'''
class Record:
    record = {}
    def __init__(self, strs):
        index_map = {}
        for index, str in enumerate(strs):
            self.update(index_map, str, index)
            index_map[str] = index

    def update(self, index_map, str, index):
        if str not in self.record:
            str_map = {}
        else:
            str_map = self.record[str]
        for key, value in index_map.items():
            if key != str:
                last_map = self.record[key]
                cur_min = index - value
                if key in str_map:
                    pre_min = str_map[key]
                    if cur_min < pre_min:
                        str_map[key] = cur_min
                        last_map[str] = cur_min
                else:
                    str_map[key] = cur_min
                    last_map[key] = cur_min

def minDistance2(str1, str2, records):
    if not str1 or not str2:
        return -1
    if len(str1) != len(str2):
        return 0
    if str1 in records and str2 in records[str1]:
        return records[str1][str2]
    return -1




















