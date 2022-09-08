'''
baekjoon s3 넷이 놀기
https://www.acmicpc.net/problem/2121

1. x값 -> y값의 형태로 점 리스트 정렬
2. 각 점에 대해서 이진탐색으로 사각형 가능 여부 확인
'''

import sys
from collections import namedtuple
input = sys.stdin.readline

# 이진탐색 구현
N = int(input())
A, B = map(int, input().split())
result = 0
dot_list = []
Point = namedtuple('Point', ['x', 'y'])
for i in range(N):
    x, y = map(int, input().split())
    dot_list.append(Point(x, y))
dot_list.sort()

def bs(l: list, target: Point) -> bool:
    start = 0
    end = len(dot_list)-1
    while start <= end:
        mid = (start + end) // 2
        if l[mid] == target:
            return True
        elif l[mid] > target:
            end = mid-1
        else :
            start = mid + 1

for dot in dot_list:
    temp = 1
    for rectangle_dot in [Point(dot.x, dot.y+B), Point(dot.x+A, dot.y), Point(dot.x+A, dot.y+B)]:
        if bs(dot_list, rectangle_dot):
            temp += 1
        else:
            break
    if temp == 4:
        result += 1

# 집합(해싱)을 통한 구현
N = int(input())
A, B = map(int, input().split())
result = 0
dot_set = set()
Point = namedtuple('Point', ['x', 'y'])
for i in range(N):
    x, y = map(int, input().split())
    dot_set.add(Point(x, y))

for dot in dot_set:
    temp = 1
    for rectangle_dot in [Point(dot.x, dot.y+B), Point(dot.x+A, dot.y), Point(dot.x+A, dot.y+B)]:
        if rectangle_dot in dot_set:
            temp += 1
        else:
            break
    if temp == 4:
        result += 1
print(result)
