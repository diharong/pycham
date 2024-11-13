import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # + 모양
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    max_value1 = 0
    for i in range(N):
        for j in range(N):
            S = arr[i][j]
            # 4방향 탐색
            for k in range(4):
                for z in range(1,M):
                    ni = i + dx[k]*z
                    nj = j + dy[k]*z
                    if 0 <= ni < N and 0 <= nj < N:
                        S += arr[ni][nj]

            if max_value1 < S:
                max_value1 = S

    # X 모양
    dx = [1, 1, -1, -1]
    dy = [-1, 1, 1, -1]

    max_value2 = 0
    for i in range(N):
        for j in range(N):
            S1 = arr[i][j]
            # 4방향 탐색
            for k in range(4):
                for z in range(1, M):
                    ni = i + dx[k] * z
                    nj = j + dy[k] * z
                    if 0 <= ni < N and 0 <= nj < N:
                        S1 += arr[ni][nj]

            if max_value2 < S1:
                max_value2 = S1

    print(f'#{tc}', max(max_value1,max_value2))

