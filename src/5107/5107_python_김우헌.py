'''
baekjoon s1 마니또
https://www.acmicpc.net/problem/5107
'''

import sys

input = sys.stdin.readline
result = []
while True:
    N = int(input())
    if N == 0:
        break
    manitto_graph = {}
    name_list = []
    chain_count = 0
    name = ''
    for i in range(N): # 마니또 그래프 생성 및 초기값 설정
        a, b = input().split()
        manitto_graph[a] = b
        name_list.append(a)
    
    while name_list: # 체인 확인
        name = name_list[0]
        chain = set()
        while True:
            if name in chain:
                chain_count += 1
                break
            chain.add(name)
            name_list.remove(name)
            name = manitto_graph[name]
    result.append(chain_count)
for index, value in enumerate(result):
    print(index+1, value)
