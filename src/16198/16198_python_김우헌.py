'''
baekjoon s1 에너지모으기
https://www.acmicpc.net/problem/16198
100 2 1 3 100
1 - n-1 번째 구슬 선택 -> 

'''
import sys

input = sys.stdin.readline

N = int(input())
beads = list(map(int, input().split()))
result = 0

def dfs(beads: list, i: int):
    beads = beads.copy()
    energy = beads[i-1]*beads[i+1]
    del beads[i]
    if len(beads) > 2:
        energy += max([dfs(beads, i) for i in range(1, len(beads)-1)])
    return energy

result = max([dfs(beads, i) for i in range(1, len(beads)-1)])
print(result)