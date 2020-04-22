# coding=utf-8

def printAllSeq(chars):
    if len(chars) == 1:
        return [chars[0]]
    res = []
    for index, char in enumerate(chars):
        temp_res = printAllSeq(chars[:index]+chars[index+1:])
        res += [char+_ for _ in temp_res]
    return res

if __name__ == '__main__':
    print(printAllSeq("abc"))
