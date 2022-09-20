import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

def getMaxEnergyInPossibleRange(lst):
    maxEnergy = 0
    for i in range(1, N-1):
        E = lst[i-1]*lst[i+1]
        if E > maxEnergy:
            maxEnergy = E
            selectIdx = i
        elif E == maxEnergy:
            selectIdx = i if lst[selectIdx] > lst[i] else selectIdx     # 에너지 같으면 더 작은거
        
    return maxEnergy, [lst[idx] for idx in range(N) if idx != selectIdx]
            
totalEnergy = 0
while N != 2:
    getEnergy, lst = getMaxEnergyInPossibleRange(lst)
    totalEnergy += getEnergy
    N -= 1

print(totalEnergy)
