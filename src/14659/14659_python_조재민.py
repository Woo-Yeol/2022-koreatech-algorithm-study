import sys
n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
temp ,result, height = 0, 0, 0
for i in data:
    if(i > height):
        height = i
        temp = 0
    else:
        temp += 1
        if (temp > result):
            result = temp
print(result)