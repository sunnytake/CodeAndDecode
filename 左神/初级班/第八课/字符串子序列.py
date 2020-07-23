# coding=utf-8

'''
对于一个字符串而言，比如：pikachu
字串是在字符串中，取出一块（连续的），如：pik, ach, kac等
子序列指的是从字符串中，顺序取出字符，但是可以不连续：如：pau, kch, icu等
'''

def process(string, index, substr, res):
    if index == len(string):
        res.append(substr)
        return
    process(string, index + 1, substr, res)
    process(string, index + 1, substr + string[index], res)


def printAllSubSequence(string):
    res = []
    process(string, 0, "", res)
    return res


if __name__ == '__main__':
    print(printAllSubSequence("abc"))
