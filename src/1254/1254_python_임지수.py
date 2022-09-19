import sys

def isPalindrome(S):
    return S == S[::-1]

input = sys.stdin.readline

S = input().rstrip()
i = 0
tmp = S

while not isPalindrome(tmp):
    tmp = S
    tmp += S[:i+1][::-1]
    i+=1

    if i == len(S)-1 : break

print(len(tmp))
