# swea. 1979. 어디에 단어가 들어갈 수 있을까

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())         # NXN    K = 단어의 길이
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):

