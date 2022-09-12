# RPG 마스터 오명진
# https://www.acmicpc.net/problem/22941

import sys
from math import ceil
Hero_HP, Hero_ATK, Villain_HP, Villain_ATK = map(int, sys.stdin.readline().split())
P, S = map(int, sys.stdin.readline().split())

Is_Skill = (0 < ((Villain_HP)%Hero_ATK) <= P) or (Hero_ATK <= P) #스킬 발동 여부

if(Is_Skill): 
    Villain_HP += S #S만큼 체력 추가

Hero_Turn = ceil(Villain_HP / Hero_ATK) #용사가 마왕을 죽이는데 걸리는 턴
Villain_Turn = ceil(Hero_HP / Villain_ATK) #마왕이 용사를 죽이는데 걸리는 턴

print('Victory!') if(Hero_Turn <= Villain_Turn) else print('gg')
    
'''
10 5 100 1
1 1
>> gg

10 7 50 1
30 10
>> Victory!
'''