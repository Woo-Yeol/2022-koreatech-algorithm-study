import sys

input = sys.stdin.readline

N, K = map(int, input().split())    # number of 주전자, 사람
volumeOfKettle = [int(input()) for _ in range(N)]
start, end = 1, sum(volumeOfKettle) // K                # max는 주전자 총 합을 K만큼 나눠줄 수 있는 값

while start <= end:
    mid = (start+end)//2                                

    result = sum([i//mid for i in volumeOfKettle])      # mid만큼 나눠줬을 때 총 줄 수 있는 사람 수 

    if result >= K:                                     # K보다 크면 더 나눠줄 수 있으므로 mid+1 부터 다시 탐색
        start = mid+1
    else:                                               # 작으면 나눠주는 용량을 낮춰야 하므로 mid-1까지로 조정 후 탐색
        end = mid-1

print(end)                                              # 탐색이 끝나면 end값이 K명에게 나눠줄 수 있는 최대의 값