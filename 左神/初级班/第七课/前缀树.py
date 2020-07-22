# coding=utf-8

class TrieNode:
    def __init__(self):
        # 经过该节点的路径数
        self.path = 0
        # 终点为该节点的路径数
        self.end = 0
        # 下一个节点
        self.nexts = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        '''
        插入单词，更新前缀树
        '''
        if not word:
            return
        node = self.root
        for char in word:
            if char not in node.nexts:
                node.nexts[char] = TrieNode()
            node = node.nexts[char]
            node.path += 1
        node.end += 1

    def search(self, word):
        '''
        查找单词是否在前缀树中存在多少次
        '''
        if not word:
            return 0
        node = self.root
        for char in word:
            if char not in node.nexts:
                return 0
            node = node.next[char]
        return node.end

    def delete(self, word):
        '''
        删除单词，更新前缀树
        '''
        node = self.root
        for char in word:
            if char in node.nexts:
                node.nexts[char].path -= 1
                if node.nexts[char].path == 0:
                    node.nexts[char] = None
                    return
            node = node.nexts[char]
        node.end -= 1

    def prefixNumber(self, pre):
        '''
        前缀个数
        '''
        if not pre:
            return 0
        node = self.root
        for char in pre:
            if char not in node.nexts:
                return 0
            node = node.nexts
        return node.path




