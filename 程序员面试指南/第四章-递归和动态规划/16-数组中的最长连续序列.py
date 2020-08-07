# coding=utf-8
'''
给定无序数组arr，返回其中最长的连续序列的长度

arr=[100, 4, 200, 1, 3, 2]，最长的连续序列为[1,2,3,4]，所以返回4

map:key代表遍历过的某个数，value代表key这个数所在的最长连续序列的长度
整个过程中，只是每个连续序列的最小值和最大值在map中的记录有意义，中间数的记录不再更新，
因为再也不会用到。这是因为我们只处理之前没出现的数，如果一个没出现的数能够把某个连续取件扩大，
或把两个连续区间连在一起，毫无疑问，只需要map中有关于这个连续区间最小值和最大值的记录
'''

def longestConsecutive(arr):
    if not arr:
        return 0
    max_val = 1
    map = {}
    for i in range(len(arr)):
        if arr[i] not in map:
            map[arr[i]] = 1
            if arr[i]-1 in map:
                max_val = max(max_val, merge(map, arr[i]-1, arr[i]))
            if arr[i]+1 in map:
                max_val = max(max_val, merge(map, arr[i], arr[i]+1))
    return max_val

def merge(map, less, more):
    '''
    只更新连续序列最小值和最大值在map中的记录即可，中间的记录不再更新，因为不会再使用。
    这是因为longestConsecutive方法的逻辑中，只处理之前没出现的数，
    如果一个没出现的数能够把某个连续区间扩大，或把某两个连续区间连在一起。
    '''
    left = less - map[less] + 1
    right = more + map[more] - 1
    length = right - left + 1
    map[left] = length
    map[right] = length
    return length

if __name__ == '__main__':
    array = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive(array))

























