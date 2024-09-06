# 12712. 파리퇴치3
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())     # NXN     M칸의 파리
    arr = [list(map(int,input().split())) for _ in range(N)]


    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_value1 = 0

    for i in range(N):
        for j in range(N):
            S = arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    ni = i + di[k]*l
                    nj = j + dj[k]*l
                    if 0 <= ni < N and 0 <= nj < N:
                        S += arr[ni][nj]

            if max_value1 < S:
                max_value1 = S



    dx = [-1, 1, 1, -1]
    dy = [1, 1, -1, -1]


    max_value2 = 0

    for x in range(N):
        for y in range(N):
            S = arr[x][y]
            for g in range(4):
                for h in range(1, M):
                    nx = x + dx[g]*h
                    ny = y + dy[g]*h
                    if 0 <= nx < N and 0 <= ny < N:
                        S += arr[nx][ny]

            if max_value2 < S:
                max_value2 = S


    # print(max_value1)
    # print(max_value2)

    result = max(max_value1,max_value2)

    print(f'#{tc} {result}')

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int,input().split())     # NXN     M칸의 파리
#     arr = [list(map(int,input().split())) for _ in range(N)]
#
#
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#
#     max_value1 = 0
#
#     for i in range(N):
#         for j in range(N):
#             S = arr[i][j]
#             for k in range(4):
#                 for l in range(1, M+1):
#                     ni = i + di[k]*l
#                     nj = j + dj[k]*l
#                     if 0 <= ni < N and 0 <= nj < N:
#                         S += arr[ni][nj]
#
#             if max_value1 < S:
#                 max_value1 = S
#
#
#
#     dx = [-1, 1, 1, -1]
#     dy = [1, 1, -1, -1]
#
#
#     max_value2 = 0
#
#     for i in range(N):
#         for j in range(N):
#             S = arr[i][j]
#             for k in range(4):
#                 for l in range(1, M+1):
#                     ni = i + dx[k]*l
#                     nj = j + dy[k]*l
#                     if 0 <= ni < N and 0 <= nj < N:
#                         S += arr[ni][nj]
#
#             if max_value2 < S:
#                 max_value2 = S
#
#
#     print(max_value1)
#     print(max_value2)
#
#     # result = max(max_value1,max_value2)
#     #
#     # print(result)