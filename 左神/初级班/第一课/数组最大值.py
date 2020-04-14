# coding=utf-8

def arrayMax(array, left, right):
    if left == right:
        return array[left]
    mid = left + (right - left) >> 1
    max_left = arrayMax(array, left, mid)
    max_right = arrayMax(array, mid+1, right)
    return max(max_left, max_right)