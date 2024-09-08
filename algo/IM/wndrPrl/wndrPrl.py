# 2반 솔빙 중계기

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # map 의 크기
    home = [list(map(int,input().split())) for _ in range(N+1)]

    num_list = []

    for i in range(len(N+1)):
        for j in range(len(N+1)):
            if home[i][j] == 2:
                repeater = (i,j)
            elif home[i][j] == 1:
                num_list.append((i,j))

    dis = []
    for x,y in num_list:
        ???



