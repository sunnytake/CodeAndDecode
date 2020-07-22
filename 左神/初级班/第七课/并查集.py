# coding=utf-8

class UnionFindSet:
    def __init__(self, nodes):
        self.father_map, self.size_map = {}, {}
        for node in nodes:
            self.father_map[node] = node
            self.size_map[node] = 1

    def findHead(self, node):
        father = self.father_map[node]
        while father != node:
            father = self.findHead(father)
        self.father_map[node] = father
        return father

    def isSameSet(self, nodea, nodeb):
        return self.findHead[nodea] == self.findHead[nodeb]

    def union(self, nodea, nodeb):
        if not nodea or not nodeb:
            return
        heada = self.findHead(nodea)
        headb = self.findHead(nodeb)
        if heada != headb:
            sizea = self.size_map[heada]
            sizeb = self.size_map[headb]
            if sizea <= sizeb:
                self.father_map[heada] = headb
                self.size_map[headb] = sizea + sizeb
            else:
                self.father_map[headb] = heada
                self.size_map[heada] = sizea + sizeb
