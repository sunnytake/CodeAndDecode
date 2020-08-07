# coding=utf-8
'''
给定两个字符串str1和str2，再给定三个整数ic、dc和rc，分别代表插入、删除和替换
一个字符的代价，返回将str1编辑成str2的最小代价
str1="abc", str2="adc", ic=5,dc=3,rc=2
从"abc"编辑成"adc"，把'b'替换成'd'是代价最小的，所以返回2
str1="abc", str2="adc", ic=5,dc=3,rc=100
从"abc"编辑成"adc"，先删除'b'，然后插入'd'是代价最小的，所以返回8
str1="abc", str2="abc", ic=5,dc=3,rc=2
不用编辑，本身就是一样的，返回0

dp[i][j]代表str1[0...i-1]编辑成str2[0...j-1]的最小代价
'''
def minCost1(str1, str2, ic, dc, rc):
    if not str1:
        return len(str2) * ic
    elif not str2:
        return len(str1) * dc
    dp = []
    for i in range(len(str1)+1):
        dp.append([0]*(len(str2)+1))
    # 第一列初始化
    for i in range(1, len(str1)+1):
        dp[i][0] = dc * i
    # 第一行初始化
    for j in range(1, len(str2)+1):
        dp[0][j] = ic * j
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # 替换代价
                dp[i][j] = dp[i-1][j-1] + rc
            # 将str1[0...i-1]先编辑为str2[0...j-2]，然后插入一个字符变为str2[0...j-1]
            dp[i][j] = min(dp[i][j], dp[i][j-1] + ic)
            # 将str1[0...i-1]删除第i个字符后变为str2[0...j-1]的代价为dp[i-1][j]+dc (str1[0..i-2] 编辑为 str2[0...j-1]的代价为dp[i-1][j])
            dp[i][j] = min(dp[i][j], dp[i-1][j] + dc)
    return dp[-1][-1]


def minCost2(str1, str2, ic, dc, rc):
    if not str1:
        return len(str2) * ic
    elif not str2:
        return len(str1) * dc
    if len(str1) >= len(str2):
        long_str, short_str = str1, str2
    else:
        long_str, short_str = str2, str1
        # str2较长就交换ic和dc的值，因为此时相当于把str2编辑为str1了
        ic, dc = dc, ic
    # 从左到右滚动更新，此时dp代表的是列
    dp = [0] * (len(short_str)+1)
    for i in range(len(short_str)+1):
        dp[i] = ic * i

    for i in range(1, len(long_str)+1):
        pre = dp[0]
        dp[0] = dc * i
        for j in range(1, len(short_str)+1):
            temp = dp[j]
            if long_str[i-1] == short_str[j-1]:
                dp[j] = pre
            else:
                dp[j] = pre + rc
            dp[j] = min(dp[j], dp[j-1] + ic)
            dp[j] = min(dp[j], temp + dc)
            pre = temp
    return dp[-1]


if __name__ == '__main__':
    str1, str2, ic, dc, rc = "abc", "adc", 5, 3, 100
    print(minCost1(str1, str2, ic, dc, rc))































