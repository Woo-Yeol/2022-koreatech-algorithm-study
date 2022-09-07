import sys

Num_Of_Index = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

data_sum = sum(data) #O(n)
result = 0

#데이터를 모두 더한 후 분배 법칙을 활용하여 풀이
for Num in data: #O(n)
    data_sum -= Num
    result += data_sum * Num
    

print(result%(10**9+7))
