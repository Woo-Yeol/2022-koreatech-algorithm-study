import sys
import math

input = sys.stdin.readline

HP_hero, ATK_hero, HP_shit, ATK_shit = map(int, input().split())
P, S = map(int, input().split())
                 
if ATK_hero <= P or 0 < HP_shit % ATK_hero <= P:        # 마왕을 잡기위해 필요한 유저 턴
    needUserTurn = math.ceil((HP_shit+S) / ATK_hero)    # 위 조건에서 스킬 발동
else:
    needUserTurn = math.ceil(HP_shit / ATK_hero)        # 스킬 발동 기회 x

needShitTurn = math.ceil(HP_hero / ATK_shit)            # 유저를 잡기위해 필요한 마왕 턴

print("Victory!") if needUserTurn <= needShitTurn else print("gg") # 유저 턴이 먼저 옴 : 같은 턴 소요시 유저 승리
