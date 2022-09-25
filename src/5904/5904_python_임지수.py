import sys

input = sys.stdin.readline

N = int(input())
moo = 'moo'
def getNofMoo(n, k, l):         # k : k번째 moo 수열이다, l : k-1번째 moo 수열 길이
    L = 2*l+(k+3)               # k번째 moo수열의 길이

    if n <= 3:                  # 종료조건 0 : 길이 3 이하면 그대로 인덱싱
        print(moo[n-1])
        exit(0)
                                # moo 수열 구간 : L(K-1) + (K+3) + L(K-1)
    if L < n:                   # 종료조건 1 : N이 첫 번째 항 구간에 존재할 때
        getNofMoo(n, k+1, L)    # 지금까지 구한 moo 수열의 길이가 N보다 작다는 것 -> 차수를 늘려 탐색
    else:                               # 종료조건 2 : 두 번째 항 구간에 존재할 때
        if n > l and n <= l+(k+3):      # m은 구간의 첫 인덱스에만 존재한다.
            print('m') if n-l == 1 else print('o')
            exit(0)
        else:                               # 종료조건 3 : 세 번째 항 구간에 존재할 때
            getNofMoo(n-(l+k+3), 1, 3)      # n에서 (l+(k+3))을 빼줌으로써 세 번째 항 구간을 첫 번째 항 구간처럼 볼 수 있게 하고
                                            # 재귀를 처음부터 돌린다(이해 안됨)
getNofMoo(N, 1, 3)
    