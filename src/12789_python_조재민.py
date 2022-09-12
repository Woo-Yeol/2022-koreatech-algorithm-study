# 도키도키 간식드리미
# https://www.acmicpc.net/problem/12789

import sys 

Num_Of_People = int(sys.stdin.readline())
Line_A = list(map(int, sys.stdin.readline().split())) #문제 상에서 "현재 줄 서있는 곳"
Line_B = [] #문제 상에서 "한 명씩만 설 수 있는 공간"
sequence = 1 #번호표 카운트

while(Line_A): #Line_A에 아무도 없을 때까지 반복
    temp = Line_A.pop(0) #Line_A에서 한 명이 출발하면
    if(temp == sequence):
        sequence += 1
    else:
        Line_B.append(temp)
        
    while(Line_B): #Line_B의 모든 사람을 점검
        if(Line_B[-1] == sequence):
            Line_B.pop()
            sequence += 1
        else:
            break

print("Sad") if(Line_B) else print("Nice")

"""
5
5 4 1 3 2
>>Nice
"""