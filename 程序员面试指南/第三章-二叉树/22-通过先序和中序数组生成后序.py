# coding=utf-8

def getPosArray(pre_vals, in_vals):
    if not pre_vals or not in_vals:
        return None
    pos_vals = [None] * len(pre_vals)
    getArray(pre_vals, 0, len(pre_vals)-1, in_vals, 0, len(in_vals)-1, pos_vals, len(pos_vals) -1)
    return pos_vals


def getArray(pre_vals, pre_start, pre_end, in_vals, in_start, in_end, pos_vals, pos_index):
    if pre_start > pre_end:
        return pos_index
    pos_vals[pos_index] = pre_vals[pre_start]
    pos_index -= 1

    index = in_vals.index(pre_vals[pre_start])
    # 先右子树
    pos_index = getArray(pre_vals, pre_start + index - in_end + 1, pre_end, in_vals, index+1, in_end, pos_vals, pos_index)
    return getArray(pre_vals, pre_start+1, pre_start + index - in_start, in_vals, in_start, index-1, pos_vals, pos_index)

if __name__ == '__main__':
    pres = [1, 2, 4, 5, 3, 6, 7]
    ins = [4, 2, 5, 1, 6, 3, 7]
    print(getPosArray(pres, ins))
















