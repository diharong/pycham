# 백준 14568. 2017 연세대학교 프로그래밍 경시대회

'''
조건
1. 남는 사탕이 없어야한다.
2. A는 B보다 2개 이상 많은 사탕을 가져야 합니다.
3. 셋 중 사탕을 하나도 못 받는 친구는 없어야 한다.
4. C가 받는 사탕의 수는 짝수이다.

'''

import sys
sys.stdin = open("input.txt")

candy = int(input()) #6
answer = 0
for A in range(0, candy+1): #0개~6개
    for B in range(0, candy + 1):  # 0개~6개
        for C in range(0, candy + 1):  # 0개~6개
            if A + B + C == candy:
                if A >= B+2:
                    if A != 0 and B != 0 and C !=0:
                        if C % 2 == 0:
                            answer += 1

print(answer)