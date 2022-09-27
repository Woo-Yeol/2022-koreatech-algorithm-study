# 에너지 모으기
# https://www.acmicpc.net/problem/16198


import sys
input = sys.stdin.readline

N, W = int(input()), [*map(int,input().split())]
result = 0

def dfs(Max):
    global result
    W_len = len(W)
    if W_len == 2:
        if result < Max:
            result = Max
        return
    else:
        for i in range(1, W_len-1):
            temp = W[i]
            W.pop(i)
            dfs(Max + (W[i-1] * W[i]))
            W.insert(i, temp)
dfs(1)
print(result)