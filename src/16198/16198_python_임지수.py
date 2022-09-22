import sys
from itertools import permutations
from copy import deepcopy

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

cases = permutations(range(1, N-1))     # 인덱스 제외 순서의 모든 경우의 수
energies = []

for case in cases:
    tmp = deepcopy(lst)                 # 다음 케이스에서 활용을 고려
    energy = 0
    removedIndex = []                   # 제외한 인덱스 관리
    for removeIndex in case:
        decreaseIndex = len([i for i in removedIndex if i < removeIndex])       # 앞에서 줄어든 만큼 인덱스 감소
        removedIndex.append(removeIndex)
        removeIndex -= decreaseIndex

        thisEnergy = tmp[removeIndex-1] * tmp[removeIndex+1]
        tmp.pop(removeIndex)
        energy += thisEnergy

    energies.append(energy)

print(max(energies))
