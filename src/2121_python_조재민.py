import sys

Num_Of_Points = int(sys.stdin.readline())
X, Y = map(int,sys.stdin.readline().split())
points = set() #리스트 구조는 탐색을 할 때 O(n)이 들지만 set은 O(1)이 든다.
for line in range(Num_Of_Points):
    a, b = map(int,sys.stdin.readline().split())
    points.add((a,b))

count = 0
for a,b in points:
    if((a + X, b) in points and 
       (a + X, b + Y) in points and 
       (a,     b + Y) in points):
        count += 1
print(count)
