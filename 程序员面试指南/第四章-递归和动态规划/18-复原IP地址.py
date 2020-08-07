# coding=utf-8
'''
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

示例:
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
'''
def splitIps(string):
    res = []
    process(string, -1, 3, [], res)
    return res

def process(string, prev_pos, left_dots, segments, res):
    for cur_pos in range(prev_pos+1, min(len(string)-1, prev_pos+4)):
        segment = string[prev_pos+1: cur_pos+1]
        if valid(segment):
            segments.append(segment)
            if left_dots - 1 == 0:
                update_output(string, cur_pos, segments, res)
            else:
                process(string, cur_pos, left_dots-1, segments, res)
            segments.pop()


def valid(segment):
    return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

def update_output(string, cur_pos, segments, res):
    segment = string[cur_pos+1:]
    if valid(segment):
        segments.append(segment)
        res.append('.'.join(segments))
        segments.pop()


if __name__ == '__main__':
    string = "25525511135"
    print(splitIps(string))


















