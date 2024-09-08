# swea. 13732 정사각형 판정

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())        # N 격자판의 크기
    arr = [list(str(input())) for _ in range(N)]

    