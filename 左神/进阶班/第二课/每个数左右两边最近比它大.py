# coding=utf-8

def getNearestLarge(array):
    res_left_large = [None]*len(array)
    res_right_large = [None]*len(array)
    stack = []
    for index, val in enumerate(array):
        while stack and array[stack[-1]] < val:
            res_right_large[stack[-1]] = val
            stack.pop()
        if stack:
            large_index = None
            for i in stack[::-1]:
                if array[i] > val:
                    large_index = i
                    break
            if large_index is not None:
                res_left_large[index] = array[large_index]
            else:
                res_left_large[index] = None
        else:
            res_left_large[index] = None
        stack.append(index)

    while stack:
        index = stack.pop()
        res_right_large[index] = None
    return res_left_large, res_right_large

if __name__ == '__main__':
    array = [4, 3, 5, 4, 3, 3, 6, 7, 9, 1, 2]
    res_left_large, res_right_large = getNearestLarge(array)
    print(res_left_large)
    print('=========================')
    print(res_right_large)


