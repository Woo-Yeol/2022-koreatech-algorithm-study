"""
https://www.acmicpc.net/problem/22941
RPG 마스터 오명진
"""
import sys
from math import ceil

input = sys.stdin.readline

hero_hp, hero_atk, devil_hp, devil_atk = map(int, input().split())
P, S = map(int, input().split())

hero_t = ceil(hero_hp / devil_atk)

res = (devil_hp - P) % hero_atk

if res > 0 and (P + res) <= hero_atk:
    devil_t = ceil(devil_hp / hero_atk)
else:
    devil_t = ceil((devil_hp + S) / hero_atk)

if hero_t >= devil_t:
    print("Victory!")
else:
    print("gg")

# while True:
#     devil_hp -= hero_atk
#     hero_hp -= devil_atk
#     if devil_hp < 0:
#         print("Victory!")
#         break
#     elif hero_hp < 0:
#         print("gg")
#         break
#     elif devil_hp >= 1 and devil_hp <= P and heal:
#         devil_hp += S
#         heal = False

# print(f"Hero HP : {hero_hp} | Devil HP : {devil_hp}")

"""
2000000000 1 2000000000 1
1000000000 1

ans: gg
"""
