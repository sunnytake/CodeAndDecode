# coding=utf-8
'''
给定数组arr,arr[i]==k代表可以从位置i向右跳1到k个距离。
比如, arr[2]=3，代表从位置2可以跳到位置3、位置4或位置5
如果从位置0出发，返回最少跳几次能跳到arr最后的位置上

arr=[3,2,3,1,1,4]
arr[0]==3，选择跳到2；arr[2]==3，可以调到最后的位置，所以返回2

jump：目前跳了多少步
cur：只能跳jump步最远能够达到的位置
next：如果再多跳一步，最远能够达到的位置

从左到右遍历arr，假设遍历到位置i
1). 如果cur >= i，说明jump步可以到达位置i，此时什么也不做
2). 如果cur < i，说明只跳jump步不能到达位置i，需要多跳一步才行，此时令
jump++，cur=next，表明多跳了一步，cur更新成跳jump+1步能够达到的位置，即next
3. 将next更新为max(next, i+arr[i])，表示下一次多跳一步到达的最远位置
'''
def jump(arr):
    if not arr:
        return 0
    jump, cur, next = 0, 0, 0
    for i in range(len(arr)):
        if cur < i:
            jump += 1
            cur = next
        next = max(next, i+arr[i])
    return jump