import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 상하좌우 델타
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    cnt = 0     # 경비의 감시를 받는 0의 개수를 담을 변수

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:  # 만약 2를 발견하면
                # 4방향 탐색시작
                for k in range(4):
                    for z in range(1, N):
                        nx = i + dx[k]*z
                        ny = j + dy[k]*z
                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                            break
                        elif 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
                            cnt += 1
    zero_cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                zero_cnt+=1

    print(zero_cnt - cnt)

















# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#
#     # 상하좌우 델타
#     dx = [0,1,0,-1]
#     dy = [1,0,-1,0]
#
#     cnt = 0     # 경비의 감시를 받는 0의 개수를 담을 변수
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 2:  # 만약 2를 발견하면
#                 # 4방향 탐색시작
#                 for k in range(4):
#                     for z in range(1, N):
#                         nx = i + dx[k]*z
#                         ny = j + dy[k]*z
#                         if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
#                             cnt += 1
#                         elif 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
#                             break
#
#
#     zero_cnt = 0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 0:
#                 zero_cnt += 1
#
#     print(zero_cnt - cnt)





































































# print('경민 is 딩초')
# print('약오르지롱 메룽메룽')