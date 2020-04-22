# coding=utf-8

def hanoi(n):
    if n > 0:
        process(n, n, "left", "mid", "right")

def process(n, form, help ,to):
    '''
    :param n: 代表1-N
    :param form:来源
    :param help:借助
    :param to:去处
    :return:
    '''
    if n == 1:
        # 只有一个，直接从from到to
        print("Move 1 from " + form + " to " + to)
    else:
        # 先将1~N-1从from到help
        process(n-1, form, help, to)
        # 将N从from到to
        print("Move " + n + " from " + form + " to " + to)
        # 将1~N-1从help到from
        process(n-1, help, to, form)