import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N x N, K = 단어길이
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j:j+K] == [1]*K:
               if (j == 0 or arr[i][j-1] == 0) and (j+K == N or arr[i][j+K]==0):
                  cnt += 1

    for j in range(N):
        for i in range(N-K+1):
            if all(arr[i+x][j] == 1 for x in range(K)):
                if (i == 0 or arr[i-1][j]==0) and (i+K == N or arr[i+K][j] == 0):
                    cnt += 1
    print(f'#{tc}', cnt)


# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int,input().split()) # N x N, K = 단어길이
#     arr = [list(map(int,input().split())) for _ in range(N)]
#
#     cnt_lst = []
#     # 가로
#     for i in range(N):
#
#         r_cnt = 0
#         for j in range(N):
#             if arr[i][j] == 0:
#                 if r_cnt > 1:
#                     cnt_lst.append(r_cnt)
#                 r_cnt = 0
#
#             elif arr[i][j] == 1:
#                 r_cnt += 1
#
#         if r_cnt > 1:
#             cnt_lst.append(r_cnt)
#
#
#     for j in range(N):
#
#         c_cnt = 0
#         for i in range(N):
#             if arr[i][j] == 0:
#                 if c_cnt > 1:
#                     cnt_lst.append(c_cnt)
#                 c_cnt = 0
#
#             elif arr[i][j] == 1:
#                 c_cnt += 1
#
#         if c_cnt > 1:
#             cnt_lst.append(c_cnt)
#
#     result = 0
#     for c in cnt_lst:
#         if c == K:
#             result += 1
#
#     print(result)





