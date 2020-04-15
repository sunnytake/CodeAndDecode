# coding=utf-8

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def netherlansFlag(array, num):
    if not array or len(array) < 2:
        return
    partition(array, 0, len(array)-1, num)

def partition(array, left, right, num):
    less, more, cur = left - 1, right + 1, left
    while cur < more:
        if array[cur] < num:
            less += 1
            swap(array, less, cur)
            cur += 1
        elif array[cur] > num:
            more -= 1
            swap(array, more, cur)
        else:
            cur += 1
    # 返回等于num区域的开始位置和结束位置
    return less+1, more-1

if __name__ == '__main__':
    array = [1, 3, 5, 7, 2, 4, 6, 5, 3, 5, 10]
    netherlansFlag(array, 5)
    print(array)