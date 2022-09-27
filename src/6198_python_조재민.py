import sys

Input = sys.stdin.readline
Num = int(Input())
data = [int(Input()) for i in range(Num)]
stack = []
result = 0
 
for i in range(Num):
    while (stack and stack[-1] <= data[i]):
        stack.pop()
 
    stack.append(data[i])
    result += len(stack) -1
 
print(result)