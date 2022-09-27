# 영상처리
# https://www.acmicpc.net/problem/21938

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
