"""
네 사람이서 2차원 평면상의 N개의 점을 이용해서 할 수 있는 놀이가 있다. 바로 각 사람이 1개씩의 점을 적절히 선택해서 변이 x축 혹은 y축에 평행한 직사각형을 만드는 일이다. 물론 그냥 만들면 재미가 없기 때문에 가로의 길이가 A 세로의 길이가 B인 직사각형을 몇 가지나 만들 수 있는지 알아보기로 했다.
예를 들어 점이 A(0, 0), B(2, 0), C(0, 3), D(2, 3), E(4, 0), F(4, 3)의 6개가 있고, 만들고 싶은 직사각형이 가로가 2, 세로가 3인 직사각형이라면 (A, B, C, D), (B, D, E, F)의 두 가지 경우가 가능하다. 모든 경우의 수를 구해보자.
"""
import sys

input = sys.stdin.readline

N = int(input())
x, y = map(int, input().split())
coordinates = set(tuple(map(int, input().split())) for _ in range(N))

count = 0
for a, b in coordinates:
    if (
        (a, b + y) in coordinates
        and (a + x, b) in coordinates
        and (a + x, b + y) in coordinates
    ):
        count += 1
print(count)
"""
6
2 3
0 0
2 0
2 3
0 3
4 0
4 3
"""
