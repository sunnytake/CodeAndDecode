# coding=utf-8
'''
字典树又称为前缀树或Trie树，是处理字符串常见的数据结构。
假设组成所有单词的字符仅是"a"~"z"，请实现字典树结构，并包含以下四个主要功能
* insert(word)：添加word，可重复添加
* delete(word)：删除word，如果word添加过多次，仅删除一个
* search(word)：查询word是否在字典树中
* prefixNumber(pre)：返回以字符串pre为前缀的单词数量
'''
class TrieNode:
    def __init__(self):
        self.path = 0 # 有多少单词共用这个节点
        self.end = 0 # 有多少单词以这个单词结尾
        self.map = {} # key为该节点的一条字符路径，value为字符路径指向的节点
        self.node = TrieNode()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if not word:
            return None
        node = self.root
        for index, char in enumerate(word):
            if char not in node.map:
                node.map[char] = TrieNode()
            node = node.map[char]
            node.path += 1
        node.end += 1

    def delete(self, word):
        if self.search(word):
            node = self.root
            for index, char in enumerate(word):
                node.map[char].path -= 1
                if node.map[char].path == 0:
                    node.map.pop(char)
                    return None
                node = node.map[char]
            node.end -= 1

    def search(self, word):
        if not word:
            return False
        node = self.root
        for index, char in enumerate(word):
            if char not in node.map:
                return False
            node = node.map[char]
        return node.end != 0

    def prefixNumber(self, pre):
        if not pre:
            return 0
        node = self.root
        for index, char in enumerate(pre):
            if char not in node.map:
                return 0
            node = node.map[char]
        return node.path
