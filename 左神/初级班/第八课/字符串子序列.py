# coding=utf-8

def printAllSubSequence(string):
    result = []
    def process(string, index, res):
        if index == len(string):
            result.append(res)
            return
        process(string, index+1, res)
        process(string, index+1, res+string[index])
    process(string, 0, "")
    return result


if __name__ == '__main__':
    print(printAllSubSequence("abc"))
