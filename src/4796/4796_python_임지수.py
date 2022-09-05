import sys
input = sys.stdin.readline

exitCase = [0, 0, 0]
cases = []
while True:
    case = list(map(int, input().split()))
    if case != exitCase:        # 0 0 0 입력시 입력 종료
        cases.append(case)
    else:
        break

for i, case in enumerate(cases):
    L, P, V = case
    print(f'Case {i+1}: {L*(V//P) + V%P}') if V%P < L \
        else print(f'Case {i+1}: {L*(V//P) + L}')
    # 기본적으로 전체 휴가를 연속하는 일로 나눈 만큼 횟수로 L일을 사용할 수 있고
    # 그 나머지만큼의 일수는 전부 사용 가능하다고 생각
    # 하지만 예를 들어 30일 휴가, 연속하는 25일 중 1일만 사용 가능하다고 할 때
    # 25일동안 1일 사용 하고, 나머지 5일에도 1일만 사용이 가능함
    # 즉, V를 P로 나눈 나머지가 L보다 작을 경우 고려를 해줘야함