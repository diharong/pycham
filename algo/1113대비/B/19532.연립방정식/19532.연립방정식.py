# 백준 19532. 수학은 비대면 강의입니다.

import sys
sys.stdin = open('input.txt')

# num_li = list(map(int,input().split()))
#
# for i in num_li:
#

A,B,C,D,E,F = map(int,input().split())

for x in range(-10000, 10001):
    for y in range(-10000, 10001):
        if A*x + B*y == C:
            if D*x + E*y == F:
                print(x,y)
                break

# 얘는 시간초과뜸
