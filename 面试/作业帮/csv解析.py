# coding=utf-8
'''
在csv解析时，会碰到各种各样的问题，如下为每行数据对应的解析结果：
aa,bb,cc                    ->>         ["aa", "bb", "cc"]
aa,"bb,cc",dd               ->>         ["aa", "bb,cc", "dd"]
aa,"bb,""cc"",dd", "ee"     ->>         ["aa", "bb,\"cc\",dd", "ee"]
'''

def parse_csv_line(line):
    res = []
    queue = []
    words = line.split(",")
    # 标志位
    flag = False
    for word in words:
        # ""c""
        if len(word) >= 4 and word[:2] == '""':
            queue.append(word[1:-1])
        # "ee"
        elif len(word) > 2 and word[0] == '"' and word[-1] == '"':
            res.append(word[1:-1])
        # "bb
        elif len(word) > 1 and word[0] == '"' and not flag:
            flag = True
            queue.append(word[1:])
        # dd"
        elif len(word) > 1 and word[-1] == '"' and flag:
            queue.append(word[:-1])
            res.append(','.join(queue))
            queue = []
            flag = False
        else:
            res.append(word)
    return res

if __name__ == '__main__':
    # aa, bb, cc -> > ["aa", "bb", "cc"]
    # aa, "bb,cc", dd -> > ["aa", "bb,cc", "dd"]
    # aa, "bb,""cc"",dd", "ee" -> > ["aa", "bb,\"cc\",dd", "ee"]
    line = "aa,bb,cc"
    print(parse_csv_line(line))
    line = "aa,\"bb,cc\",dd"
    print(parse_csv_line(line))
    line = "aa,\"bb,\"\"cc\"\",dd\",\"ee\""
    print(parse_csv_line(line))






















