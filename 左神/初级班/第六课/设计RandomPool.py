# coding=utf-8

"""
设计一种结构，在该结构中有如下三个功能：
insert(key)：将某个key加入到该结构，做到不重复加入
delete(key)：将原本在结构中的某个key移除
getRandom()：等概率随机返回结构中的任何一个key
要求：insert,delete,getRandom方法的时间复杂度都是O(1)
"""
import random


class RandomPool:
    map_str2index = {}
    map_index2str = {}
    index = 0

    def insert(self, key):
        if key not in self.map_str2index:
            self.map_str2index[key] = self.index
            self.map_index2str[self.index] = key
            self.index += 1

    def delete(self, key):
        if key in self.map_str2index:
            temp_index = self.map_str2index[key]
            new_key = self.map_index2str[self.index-1]
            self.map_str2index[new_key] = temp_index
            self.map_index2str[temp_index] = new_key
            self.index -= 1

    def getRandom(self):
        random_index = int(random.random() * self.index)
        return self.map_index2str[random_index]

