import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int,input().split()) # N x N, K = 단어길이
#     arr = [list(map(int,input().split())) for _ in range(N)]
#
#     result = 0
#     for i in range(N):
#         for j in range(N-K+1):
#             if arr[i][j:j+K] == [1]*K:
#                 if (j==0 or arr[i][j-1] == 0) and (j+K == N or arr[i][j+K] == 0):
#                     result += 1
#
#     for j in range(N):
#         for i in range(N-K+1):
#             if all(arr[i+x][j]==1 for x in range(K)):
#                 if (i==0 or arr[i-1][j]==0) and (i+K==N or arr[i+K][j]==0):
#                     result += 1
#
#     print(result)
#
#

# T = int(input())
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())  # N x N, K = 단어길이
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     cnt_lst = []
#     # 가로 순회
#     for i in range(N):
#         cnt_r = 0
#         for j in range(N):
#             if arr[i][j] == 1:
#                 cnt_r += 1
#
#             else:       # 만약 0일 경우에는 1. 먼저, (연속된 1의 길이를 더 이상 이어갈 수 없다.)
#                 # 0 전에 길이카운트한 것이 있는지 확인하는 코드
#                 if cnt_r > 1:   # 만약에 이전에 1을 카운트 한 값이 있으면? (2이상일때)
#                     cnt_lst.append(cnt_r)   # 그 값을 cnt_lst 에 넣어준다.
#                 cnt_r=0  # 1. 카운트를 0으로 초기화하는데 그전에 위의 if문 다시 확인
#
#         # 행 하나가 끝났을 때 최종적으로 연속된 '1' 의 길이를 확인하는 코드
#         if cnt_r > 1:   # 만약에, cnt값이 2이상이면
#             cnt_lst.append(cnt_r)   # 그것도 연속된 길이로 간주하고 리스트에 넣어준다.
#
#     print(cnt_lst)
#
#     # 세로순회
#     for j in range(N):
#         cnt_c = 0
#         for i in range(N):
#             if arr[i][j] == 1:
#                 cnt_c += 1
#             else:
#                 if cnt_c > 1:
#                     cnt_lst.append(cnt_c)
#                 cnt_c = 0
#         if cnt_c > 1:
#             cnt_lst.append(cnt_c)
#
#     cnt = 0
#     for k in cnt_lst:
#         if k == K:
#             cnt += 1
#     print(cnt)
#









    # result = 0
    # for i in range(N):  # 행을 순회
    #     for j in range(N-K+1):
    #         # if j+K < N:
    #         if arr[i][j:j+K] == [1]*K:  # K 로 하면 안되고 [1]*K 로 해서 배열자체가 동일한지 확인
    #             # 조건이 맞는지, 범위에 들어있는지 확인
    #             if arr[i][j+K-1] == 0 and arr[i][j+K+1] == 0:
    #                 result += 1
    #
    #         # print(arr[i][j:j+K])
    #         # print([1]*K)
    #         # print(len(arr[i][j:j+K])) 이건 아님 1의 개수가 아니라 진짜 배열로 출력됨
    #
    # print(result)

























    # # K개만큼 1로 채워진 배열 만들기
    # words = [ 1 for _ in range(K)]
    #
    # # print(words)
    #
    # for i in range(N):  # 행 순회
    #     for j in range(N):  # 열 순회
    #         if arr[i][j:j+K] == words:
    #






    # # print(N, K)
    #
    # # 제로패딩코드
    # padded_array = [[0]*(N+2) for _ in range(N+2)]
    #
    # for i in range(N):
    #     for j in range(N):
    #         padded_array[i+1][j+1] = arr[i][j]
    #
    # # print(padded_array)
    #
    # # 행 - [0,1,1,1,0] 과 같은 배열 찾기
    # for i in range(N+2):
    #     for j in range(N+2):
    #         if padded_array[i][j]
    #


