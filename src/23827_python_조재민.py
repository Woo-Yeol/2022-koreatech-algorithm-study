# 수열 (Easy)
# https://www.acmicpc.net/problem/23827

import sys

Num_Of_Index = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

data_sum = sum(data) #O(n)
result = 0

# 입력 받은 데이터를 sum 함수를 사용해 모두 더한 후
# 분배 법칙( (a+b)*c = ac + bc )을 활용하여 코드를 작성했습니다

for Num in data: #O(n)
    data_sum -= Num
    result += data_sum * Num
    

print(result%(10**9+7))


"""
3
1 2 3
>> 11
"""
