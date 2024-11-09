import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    stack = []
    result = []

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                stack.append(1)
            else:
                if len(stack) != 0:
                    result.append(len(stack))
                stack = []

        if len(stack) != 0:
            result.append(len(stack))
            stack = []
    if len(result) == 0:
        result = [0]


    for j in range(M):
        for i in range(N):
            if arr[i][j] == 1:
                stack.append(1)
            else:
                if len(stack) != 0:
                    result.append(len(stack))
                stack = []

        if len(stack) != 0:
            result.append(len(stack))
            stack = []
    if len(result) == 0:
        result = [0]

    print(f'#{tc}', max(result))











# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int,input().split())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#
#     # 가로 탐색
#     r_cnt = 0   # 가로 탐색시 발견한 1을 카운트할 변수
#     result = []     # 발견된 구조물의 길이 담을 리스트
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 1:
#                 r_cnt += 1
#             else:
#                 if r_cnt >= 1:
#                     result.append(r_cnt)
#                 r_cnt = 0
#
#         if r_cnt >= 1:
#             result.append(r_cnt)
#
#     if len(result) == 0:
#         result = [0]
#
#     # 세로 탐색
#     # 발견된 구조물의 길이 담을 리스트
#     for j in range(M):
#         c_cnt = 0
#         for i in range(N):
#             if arr[i][j] == 1:
#                 c_cnt += 1
#             else:
#                 if c_cnt >= 1:
#                     result.append(c_cnt)
#                 c_cnt = 0
#
#         if c_cnt >= 1:
#             result.append(c_cnt)
#
#     if len(result) == 0:
#         result = [0]
#
#
#     print(f'#{tc}', max(result))
