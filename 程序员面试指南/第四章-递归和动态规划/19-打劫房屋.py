# coding=utf-8
'''
打劫房屋1：
假设你是一个专业的窃贼，准备沿着一条街打劫房屋。每个房子都存放着特定金额的钱。你面临的唯一约束条件是：
相邻的房子装着相互联系的防盗系统，且 当相邻的两个房子同一天被打劫时，该系统会自动报警。
给定一个非负整数列表，表示每个房子中存放的钱， 算一算，如果今晚去打劫，你最多可以得到多少钱 在不触动报警装置的情况下。

给定 [3, 8, 4], 返回 8.

前提：对于某一间房子i，如果盗贼要打劫该房子，则房间对序号为i-1的房子（即前一所房子）盗贼不能进行打劫才能保证系统不报警。
因此，很容易得出动态规划的表达式：
1.建立一个数组DP[]，DP[i]用来表示盗贼打劫到第i所房子时所能获得的最大金额数；
2.根据前提的描述，盗贼不打劫当前房子，则DP[i] = DP[i-1]；否则DP[i] = DP[i-2] + A[i]；
因此DP[i] = max{ DP[i-1], DP[i-2] + A[i]}；
'''
def houseRobber1(array):
    if not array:
        return 0
    if len(array) == 1:
        return array[0]

    dp = [0] * len(array)
    dp[0] = array[0]
    dp[1] = max(array[0], array[1])

    for i in range(2, len(array)):
        dp[i] = max(dp[i - 1], dp[i - 2] + array[i])
    return dp[-1]

'''
在上次打劫完一条街道之后，窃贼又发现了一个新的可以打劫的地方，但这次所有的房子围成了一个圈，这就意味着第一间房子和最后一间房子是挨着的。
每个房子都存放着特定金额的钱。你面临的唯一约束条件是：相邻的房子装着相互联系的防盗系统，且 当相邻的两个房子同一天被打劫时，该系统会自动报警。
给定一个非负整数列表，表示每个房子中存放的钱， 算一算，如果今晚去打劫，你最多可以得到多少钱 在不触动报警装置的情况下。

注意事项：
这题是House Robber的扩展，只不过是由直线变成了圈。
样例：
给出nums = [3,6,4], 返回　6，　你不能打劫3和4所在的房间，因为它们围成一个圈，是相邻的。
算法分析：
本题在打劫房屋I的基础上增加了一个条件就是第一所房子与最后一所房子也不能兼得，其实本质并没有发生变化。
在I中我们的建立的动态规划数组为DP[i]表示盗贼打劫到第i所房子获利的最大值，
因此我们同样可以建立两个数组dp1和dp2分别用来记录打劫区间为[1, n-1] 与 [2,n]的获利情况。
这是因为第一所房子与最后一所房子不能够相邻，因此将其分为两个区间[1,n-1]与[2,n]后则就将问题化为了直线的打劫问题，也就可以运用I中的方法求解。
'''


def houseRobber2(array):
    if not array or len(array) == 2:
        return 0
    if len(array) == 1:
        return array[0]

    # 从第1个到n-1个，下标为0到n-2
    dp1 = [0] * (len(array) - 1)
    # 从第2个到n个，下标为1到n-1
    dp2 = [0] * (len(array) - 1)

    for i in range(len(array) - 1):
        if i == 0:
            dp1[0] = array[0]
        elif i == 1:
            dp1[i] = max(dp1[0], array[1])
        else:
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + array[i])

    for i in range(1, len(array)):
        if i == 1:
            dp2[i - 1] = array[1]
        elif i == 2:
            dp2[i - 1] = max(dp2[0], array[2])
        else:
            dp2[i - 1] = max(dp2[i - 2], dp2[i - 3] + array[i])
    return max(dp1[-1], dp2[-1])


'''
在上次打劫完一条街道之后和一圈房屋之后，窃贼又发现了一个新的可以打劫的地方，但这次所有的房子组成的区域比较奇怪，
聪明的窃贼考察地形之后，发现这次的地形是一颗二叉树。与前两次偷窃相似的是每个房子都存放着特定金额的钱。
你面临的唯一约束条件是：相邻的房子装着相互联系的防盗系统，且当相邻的两个房子同一天被打劫时，该系统会自动报警。
算一算，如果今晚去打劫，你最多可以得到多少钱，当然在不触动报警装置的情况下。

样例：
  3
 / \
2   3
 \   \ 
  3   1
窃贼最多能偷窃的金钱数是 3 + 3 + 1 = 7.
    3
   / \
  4   5
 / \   \ 
1   3   1
窃贼最多能偷窃的金钱数是 4 + 5 = 9.

算法分析：
打劫房屋I、II均为对数组的动态规划处理，但本题是要求对二叉树进行一个动态规划处理。对于本题，首先要了解怎样是相邻：
有直接连接的节点之间算相邻节点，即父节点与亲子节点；
对于二叉树中的某一个节点i，它也有偷与不偷这两个选项，若偷，则两个子节点不能偷；否则，两个子节点可以偷。
与I、II不同的是，I、II中对当前的房屋i，偷与不偷仅需把其中的较大者保留下来进行，
因为后序的结果均是建立在前者为最优解的基础上进行的，而且DP[i] = max{DP[i-1],DP[i-2]+A[i]}一定能保证不发生冲突；
但是对于二叉树，当前节点i并不能那么方便的找到其子节点的子节点的最优解，因此并不能同I、II那样仅记录最优解。
对于二叉树的节点而言，其最容易访问到的就是它的两个子节点。
因此，可以建立一个大小为2的一维数组DP，其中DP[0]用来记录偷当前节点所能获利值，DP[1]用来记录不偷当前的值所能获利的值。
因为二叉树由根节点开始进行发散，因此可以用后序遍历的方式最终返回一个二维数组。
动态规划表达式如下：
对于某一个节点node，若偷：DP[0] = left[1] + right[1] + node.val; 
若不偷：DP[1] = max{left[0],left[1]} + max{right[0],right[1]};
'''

def houseRobber3(root):
    result = posOrder(root)
    return max(result)

def posOrder(root):
    if not root:
        return [0, 0]
    result = [0, 0]
    left = posOrder(root.left)
    right = posOrder(root.right)
    # 偷当前节点
    result[0] = left[1] + right[1] + root.val
    # 不偷当前节点
    result[1] = max(left[0], left[1]) + max(right[0], right[1])
    return result

if __name__ == '__main__':
    array = [3, 8, 4]
    print(houseRobber1(array))
    array = [3, 6, 4]
    print(houseRobber2(array))


















