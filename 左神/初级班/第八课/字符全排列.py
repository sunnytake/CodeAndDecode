# coding=utf-8

def printAllSeq(chars):
    if len(chars) == 1:
        return [chars[0]]
    res = []
    for index, char in enumerate(chars):
        temp_res = printAllSeq(chars[:index] + chars[index + 1:])
        res += [char + _ for _ in temp_res]
    return res


def printAllSeq2(string):
    res = []
    process(string, res, "")
    return res

def process(string, res, temp_str):
    if not string:
        res.append(temp_str)
        return
    for index, char in enumerate(string):
        process(string[:index] + string[index + 1:], res, temp_str + char)


if __name__ == '__main__':
    print(printAllSeq("abc"))
    print(printAllSeq2("abc"))
