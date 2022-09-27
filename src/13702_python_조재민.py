# 이상한 술집
# https://www.acmicpc.net/problem/13702

import sys
input = sys.stdin.readline

Kettle, People = map(int,input().split())
ml = []
for _ in range(Kettle):
    ml.append(int(input()))

Min = 1
Max = sum(ml)//People #Max의 시작점은 총 ml를 사람 수로 나눈 것을 넘어갈 수 없다.

#이진 분류 활용
while(Min<=Max):
    middle = (Min + Max) // 2

    dist = sum(i//middle for i in ml)
        
    if(dist >= People):
        Min = middle + 1
    else:
        Max = middle - 1

print(Max)

"""
2 3
702
429
>>351

4 11
427
541
774
822
>>205
"""