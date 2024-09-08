# swea 1861.정사각형 방

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_value = 1

    for i in range(N):

        for j in range(N):
            cnt = 1
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[i][j]+1:
                    cnt += 1

        if max_value < cnt:
            max_value = cnt

    print(f'#{tc} {max_value}')