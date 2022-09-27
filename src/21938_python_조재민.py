# 영상처리
# https://www.acmicpc.net/problem/21938

1. 처음에 문제를 풀 때 dfs와 bfs를 생각하지 못하고 무작정 풀다가 계속 실패했습니다 -> dfs 적용
2. numpy를 활용해서 zero padding을 간단하게 하려다가 백준에서는 numpy를 못쓰는 걸 알게됐습니다 -> 손수 zero padding함
3. dfs를 적용했지만 재귀가 많아지면서 Recursion ERROR가 떴습니다 -> sys.setrecursionlimit(10**9) 선언
4. 재귀가 많아지다보니 시간이 오래걸려 비효율적인 코드가 작성됐습니다 -> bfs로 변경해야하는데 귀찮아서 안함
5. 억까 그 자체

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9) #Recursion ERROR 방지용, 재귀가 많아지면 에러 뜸

N, M = map(int,input().split())
data, Pixels= [], []

for _ in range(N):
    data.append(list(map(int,input().split())))

T = int(input())

#Pixel들을 임계값(T)를 기준으로 1과 0으로 변형하고 상하좌우 비교를 위해 zero padding을 함
Pixels = [[0 for _ in range(M+2)]]
for data in data:
    avg = [0]
    for i in range(0, 3*M , 3):
        temp  = (data[i] + data[i+1] + data[i+2])/3
        avg.append(1) if (temp >= T) else avg.append(0)
    avg.append(0)
    Pixels.append(avg)
Pixels.append([0 for _ in range(M+2)])

check_list = [[1,0],[0,1],[0,-1],[-1,0]]
Object_cnt = 0

#상하 좌우 비교, 1인 픽셀이 인접해 있음 그 좌표(i,j)를 저장
def check_Pixel(Pixels, i, j):
    check_result = []
    for check in check_list:
        if(Pixels[i+check[0]][j+check[1]]):
            check_result.append([i+check[0],j+check[1]])
    return check_result

#dfs
def dfs(Pixels, i, j):
    Pixels[i][j]=0
    check_result = check_Pixel(Pixels, i, j)
    for check in check_result:
        dfs(Pixels, check[0], check[1])
    return Pixels

#픽셀들에 적용
for i in range(1,N+1):
    for j in range(1,M+1):
        if(Pixels[i][j]):
            Pixels = dfs(Pixels, i, j)
            Object_cnt += 1

print(Object_cnt)