# 2반 솔빙 시험지 채점

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    right_answer = list(map(int,input().split()))
    student = [list(map(int, input().split())) for _ in range(N)]

