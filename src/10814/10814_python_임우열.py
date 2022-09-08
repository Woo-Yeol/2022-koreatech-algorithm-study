"""
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 
이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.
"""
import sys

input = sys.stdin.readline

count = int(input())

dic = list()
for i in range(count):
    dic.append(input().split())

dic.sort(key=lambda x: int(x[0]))
for k, v in dic:
    print(f"{k} {v}")

"""
3
21 Junkyu
21 Dohyun
20 Sunyoung
"""
"""
5
21 abcdef
21 abcdeg
21 Junkyu
21 Dohyun 
20 Sunyoung
"""
