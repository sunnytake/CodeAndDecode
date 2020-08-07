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
    '''
    函数含义：如果array[i...j]这个排列上的纸牌被绝顶聪明的人先拿，最终能获得什么分数。
    分析first(i, j)：
    1.如果i==j，即array[i...j]上只剩一张纸牌。当然会被先拿纸牌的人拿走，所以返回array[i]
    2.如果i!=j。当前拿纸牌的人有两种选择，要么拿走array[i]，要么拿走array[j]。
    如果拿走array[i]，那么排列将剩下array[i+1...j]。对当前的玩家来说，面对array[i+1...j]
    排列的纸牌，他成了后拿的人，所以后续他能获得的分数为last(i+1,j)。
    如果拿走array[j]，那么排列将剩下array[i...j-1]。对当前的玩家来说，面对array[i...j-1]
    排列的纸牌，他成了后拿的人，所以后续他能获得分数为last(i, j-1)。
    作为绝顶聪明的人，必然会在两种决策中选最优的，所以返回max(array[i]+last(i+1,j), array[j]+last(i, j-1))
    '''
    # 模仿A的行为
    if start == end:
        return arr[start]
    return max(arr[start] + last(arr, start+1, end), arr[end] + last(arr, start, end-1))

def last(arr, start, end):
    '''
    函数含义：如果array[i...j]这个排列上的纸牌被绝顶聪明的人后拿，最终能获得什么分数。
    1.如果i==j，即array[i...j]上只有一张牌。作为后拿牌的人必然什么也得不到，返回0
    2.如果i!=j。根据函数last的定义，玩家的对手会先拿纸牌。对手要么拿走array[i]，要么拿走array[j]。
    如果对手拿走array[i]，那么排列将剩下array[i+1...j]，然后伦到玩家先拿。
    如果对手拿走array[j]，那么排列将剩下array[i...j-1]，然后伦到玩家先拿。
    对手也是绝顶聪明的人，所以必然会把最差的情况留给玩家
    '''
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






























