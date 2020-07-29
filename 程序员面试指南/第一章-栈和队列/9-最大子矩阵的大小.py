# coding=utf-8
'''
给定一个整型矩阵map，其中的值只有0和1两种，求其中全是1的所有矩形区域中，
最大的矩形区域为1的数量。
例如：
1   1   1   0
其中，最大的矩形区域有3个1，所以返回3
再如：
1   0   1   1
1   1   1   1 => 2  1   2   2
1   1   1   0 => 3  2   3   0
其中，最大的矩形区域有6个1，所以返回6
'''
def maxRecSize(mat):
    if not mat or not mat[0]:
        return 0
    maxArea = 0
    highs = [0] * len(mat[0])
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                highs[j] = 0
            else:
                highs[j] += mat[i][j]
        maxArea = max(maxArea, maxRecFromBottom(highs))
    return maxArea

def maxRecFromBottom(highs):
    if not highs:
        return 0
    maxArea = 0
    # 栈顶到栈底依次递减
    stack = []
    for i in range(len(highs)):
        while stack and highs[stack[-1]] >= highs[i]:
            # 下标为j的元素弹出，说明碰到了小于等于highs[j]的元素，相当于此时碰到了右边界
            # 等于时，可以确定以highs[i]扩展的矩形面积一定等于以highs[j]扩展的矩形面积，所以也弹出
            j = stack.pop()
            if not stack:
                k = -1
            else:
                k = stack[-1]
            curArea = (i - k - 1) * highs[j]
            maxArea = max(curArea, maxArea)
        stack.append(i)
    while stack:
        j = stack.pop()
        if not stack:
            k = -1
        else:
            k = stack[-1]
        curArea = (len(highs) - k - 1) * highs[j]
        maxArea = max(curArea, maxArea)
    return maxArea

if __name__ == '__main__':
    mat = [[1, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]]
    print(maxRecSize(mat))

















