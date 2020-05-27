# coding=utf-8
'''
给定一个整形数组arr，代表数值不同的纸牌排成一条线。
玩家A和玩家B依次拿走每张纸牌，规定玩家A先拿，玩家B后拿，但是每个玩家每次只能拿走
最左或者最右的纸牌，玩家A和玩家B都绝顶聪明，请返回最后获胜者的分数

arr=[1,2,00,4]
开始时玩家A只能拿走1或4
如果玩家A拿走1，则排列变为[2,100,4]，接下来玩家B可以拿走2或4，然后继续轮到玩家A
如果开始时玩家A拿走4，则排列变为[1,2,100]，接下来玩家B可以拿走1或100，然后继续轮到玩家A。
玩家A作为绝顶聪明的人不会先拿4，因为拿4之后，玩家B将拿走100。
所以玩家A会先拿1，让排列变成[2,100,4]，接下来玩家B不管怎么选，100都会被玩家A拿走，玩家A会获胜，
分数为101.
arr=[1,100,2]
开始时玩家A不管拿1还是2，玩家B作为绝顶聪明的人，都会把100拿走。玩家B会获胜，分数为100，所以返回100
'''

'''
暴力递归：递归函数N层，first和last是交替出现的
first(i,j)会有last(i+1,j)和last(i,j-1)两个递归分支
last(i,j)也会有first(i+1,j)和first(i,j-1)两个递归分支
所以整体的时间复杂度为O(2^N)，额外空间复杂度为O(N)
'''
def win1(arr):
    if not arr:
        return 0
    return max(first(arr, 0, len(arr)-1), last(arr, 0, len(arr)-1))

def first(arr, start, end):
    # 模仿A的行为
    if start == end:
        return arr[start]
    return max(arr[start] + last(arr, start+1, end), arr[end] + last(arr, start, end-1))

def last(arr, start, end):
    # 模仿B的行为
    if start == end:
        return 0
    return min(first(arr, start+1, end), first(arr, start, end-1))


'''
动态规划：
如果arr长度为N，生成两个大小为NxN的矩阵first_mat和last_mat
first_mat[i][j]表示函数first(i,j)的返回值
last_mat[i][j]表示函数last(i,j)的返回值
时间复杂度为O(N^2)，空间复杂度为O(N^2)
'''
def win2(arr):
    if not arr:
        return 0
    first_mat, last_mat = [], []
    for i in range(len(arr)):
        first_mat.append([0]*len(arr))
        last_mat.append([0]*len(arr))

    for j in range(len(arr)):
        first_mat[j][j] = arr[j]
        for i in range(j-1, -1, -1):
            first_mat[i][j] = max(arr[i] + last_mat[i+1][j], arr[j] + last_mat[i][j-1])
            last_mat[i][j] = min(first_mat[i+1][j], first_mat[i][j-1])
    return max(first_mat[0][-1], last_mat[0][-1])






























