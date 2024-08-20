import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_value = 0
    for i in range(N):
        for j in range(M):
            S = arr[i][j]
            for k in range(len(di)):
                for z in range(1, arr[i][j]+1):
                    ni = i + di[k]*z
                    nj = j + dj[k]*z
                    if 0 <= ni < N and 0 <= nj < M:
                        S += arr[ni][nj]

            if max_value < S:
                max_value = S
    print(max_value)