import sys

input = sys.stdin.readline

N = int(input())
num_lst = list(map(int, input().split()))
weight_sum = sum(num_lst)
result = 0

for num in num_lst:
    weight_sum -= num
    result += num*weight_sum
print(result%1000000007)