# coding=utf-8
'''
如果一个字符串str，把字符串str前面任意的部分挪到后面形成的字符串叫做str的旋转词。
比如str="12345"，str的旋转词有"12345"、"23451"、"34512"、"45123"和"51234"。
给定两个字符串a和b，请判断a和b是否互为旋转词

a="cdab", b="abcd"，返回True
a="1ab2", b="ab12"，返回False
a="2ab1", b="ab12"，返回True
'''
def isRotation(a, b):
    if not a or not b or len(a) != len(b):
        return False
    double_b = b + b
    return double_b.find(a) != -1















