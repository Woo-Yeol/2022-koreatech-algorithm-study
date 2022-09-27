# 팰린드롬 만들기
# https://www.acmicpc.net/problem/1254

import sys
str = input()
length = len(str)

for i in range(length):
    slice = str[i:]
    if ( slice == slice[::-1] ):
        print(length+i)
        break

"""
abab
>>5

abacaba
>>7

qwerty
>>11

abdfhdyrbdbsdfghjkllkjhgfds
>>38
"""