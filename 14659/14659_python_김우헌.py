'''
baekjoon b1 한조서열정리하고옴ㅋㅋ
https://www.acmicpc.net/problem/14659
한 봉우리에서 순차적으로 이동해 자신보다 큰 봉우리를 만나면
현재까지의 처치 수를 최대값과 비교해 더 큰 값을 저장한다.
이후 그 큰 봉우리부터 시작해 반복한다.
'''

import sys
input = sys.stdin.readline

N = int(input())
m = list(map(int, input().split()))

start = 0
max_kill = 0
while start < N-1:
    current_height = m[start]
    current_kill = 0
    for i in range(start+1, N):
        if current_height > m[i]:
            current_kill += 1
        else:
            break
    max_kill = max(max_kill, current_kill)
    start = i
print(max_kill)
        
