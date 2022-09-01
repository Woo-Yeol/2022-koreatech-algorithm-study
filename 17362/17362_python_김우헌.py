'''
baekjoon b4 수학은 체육과목 입니다 2
https://www.acmicpc.net/problem/17362
해당 문제의 손가락은 1234 - 5432 - 1234 - 5432 의 반복으로 이루어짐
'''

import sys
input = sys.stdin.readline

partten = [1, 2, 3, 4, 5, 4, 3, 2]

def solution(n):
    return partten[n % 8 - 1]

n: int = int(input())
print(solution(n))