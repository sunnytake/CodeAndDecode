# coding=utf-8

def manacher(string):
    string = '#' + '#'.join(string) + '#'
    # 回文半径数组
    recur_length = [0]*len(string)
    max_right = 0
    pos = 0
    max_length = 0
    for index in range(len(string)):
        if index < max_right:
            # index在max_right左边
            recur_length[index] = min(recur_length[2*pos-index], max_right-index)
        else:
            # index在max_right右边，以index为中心的回文串还没扫到，此时以index为中心向两边扩展
            recur_length[index] = 1

        # 以index为中心向两边扩展，知道达到边界或者左!=右
        while index - recur_length[index] >= 0 and index + recur_length[index] < len(string) and string[index-recur_length[index]] == string[index + recur_length[index]]:
            recur_length[index] += 1

        # 更新max_length和pos
        if index + recur_length[index] - 1 > max_right:
            max_right = index + recur_length[index] - 1
            pos = index

        # 更新最长回文子串的长度
        max_length = max(max_length, recur_length[index])
    # 返回最长回文串
    recur_str = string[recur_length.index(max_length)-max_length+1 : recur_length.index(max_length)+max_length-1]
    return recur_str.replace('#', '')

print(manacher("cbbd"))