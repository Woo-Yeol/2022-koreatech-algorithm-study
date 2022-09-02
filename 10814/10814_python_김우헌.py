'''
baekjoon s5 나이순정렬
https://www.acmicpc.net/problem/10814
'''
import sys
input = sys.sdtin.readline

N = int(input())
user_list = []
for i in range(N):
    age, name = input().split()
    user_list.append([i, int(age), name])
user_list.sort(key = lambda x: (x[1], x[0]))
for u in user_list:
    print(str(u[1]) + ' ' + u[2])
