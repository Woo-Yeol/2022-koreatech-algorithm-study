"""
https://www.acmicpc.net/problem/12789
도키도키 간식드리미
"""
import sys

input = sys.stdin.readline

N = int(input())
ary = list(map(int, input().split()))
ary.reverse()

stack, turn = list(), 1

while ary:
    if ary[-1] == turn:
        ary.pop()
        turn += 1
    elif stack and stack[-1] == turn:
        stack.pop()
        turn += 1
    else:
        stack.append(ary.pop())

while stack:
    if stack.pop() == turn:
        turn += 1
    else:
        print("Sad")
        break

if turn > N:
    print("Nice")
