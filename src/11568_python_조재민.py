# 민균이의 계략
# https://www.acmicpc.net/problem/11568

#해답 참조

import bisect
n = int(input())
arr = (int(x) for x in input().strip().split())
C = []
for num in arr:
    if C and C[-1] >= num:
        C[bisect.bisect_left(C,num)] = num
    else:
        C.append(num)
        
print(len(C))




'''
5
8 9 1 2 10
>> 3

8
5 4 3 2 1 6 7 8
>> 4
'''