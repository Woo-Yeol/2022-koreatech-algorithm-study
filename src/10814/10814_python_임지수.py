N = int(input())
lst = [(input().split(),i) for i in range(N)]                   # input 정보와 가입한 순서를 튜플형태로 리스트에 저장
for l in sorted(lst, key = lambda x : (int(x[0][0]),x[1])):     # 정렬 : 우선순위 나이 -> 가입한 순서
    print(l[0][0], l[0][1])

