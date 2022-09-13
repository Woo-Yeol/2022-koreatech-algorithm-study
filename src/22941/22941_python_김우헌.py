'''
baekjoon s2 RPG 마스터 오명진
https://www.acmicpc.net/problem/22941
1. 마왕이 체력을 회복할 수 있는지 확인 -> 체력회복한다면 마왕체력에 S 더하기
- 기준점 P보다 공격력이 낮거나, 치다가 0<n<P 사이의 체력 n 이 될 경우 무조건 체력회복
2. 마왕 잡는데 걸리는 턴수 <= 유저 죽는데 걸리는 턴수 라면 승리
'''

import sys
import math
input = sys.stdin.readline

a_hp, a_power, b_hp, b_power = map(int, input().split())
P, S = map(int, input().split())

if a_power <= P or 0 < b_hp % a_power <= P:
    b_hp += S

print('Victory!') if math.ceil(b_hp / a_power) <= math.ceil(a_hp / b_power) else print('gg')