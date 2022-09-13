'''
baekjoon s2 RPG 마스터 오명진
https://www.acmicpc.net/problem/22941
1. 마왕을 죽이는데 소요되는 턴 계산 (마왕체력 // 용사공격력)
'''

import sys
import math
input = sys.stdin.readline

a_hp, a_power, b_hp, b_power = map(int, input().split())
P, S = map(int, input().split())

if not a_power >= b_hp and 0 < b_hp - a_power <= P: #(b_hp - P) % a_power + P >= a_power:
    b_hp += S

print('Victory!') if math.ceil(b_hp / a_power) <= math.ceil(a_hp / b_power) else print('gg')
