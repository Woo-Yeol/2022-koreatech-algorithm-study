N = int(input())
lst = [(input().split(),i) for i in range(N)]
for l in sorted(lst, key = lambda x : (int(x[0][0]),x[1])):     # 나이 int로 type변환 해줘야 모든 케이스에서 정확한 정렬
    print(l[0][0], l[0][1])

'''
3
21 Junkyu
21 Dohyun
20 Sunyoung
'''
