import sys

input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))
check = [0 for _ in range(200000)]
results=[]
i, j = 0, 0

while j < N:
    if check[lst[j]] < K:
        check[lst[j]] += 1
        j += 1
    else:
        check[lst[i]] -= 1
        i += 1
    results.append(j-i)
print(max(results))
