import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split()) # N x N, K = 단어길이
    arr = [list(map(int,input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N-K+1):
            if arr[i][j:j+K] == [1]*K:
                if (j==0 or arr[i][j-1] == 0) and (j+K == N or arr[i][j+K] == 0):
                    result += 1

    for j in range(N):
        for i in range(N-K+1):
            if all(arr[i+x][j]==1 for x in range(K)):
                if (i==0 or arr[i-1][j]==0) and (i+K==N or arr[i+K][j]==0):
                    result += 1

    print(result)

    cnt_lst = []

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N x N, K = 단어길이
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가로 순회
    for i in range(N):
        cnt_r = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt_r += 1
            else:
                if cnt_r > 1:
                    cnt_lst.append(cnt_r)
                cnt_r=0
        if cnt_r > 1:
            cnt_lst.append(cnt_r)

    # 세로순회
    for j in range(N):
        cnt_c = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt_c += 1
            else:
                if cnt_c > 1:
                    cnt_lst.append(cnt_c)
                cnt_c = 0
        if cnt_c > 1:
            cnt_lst.append(cnt_c)

    cnt = 0
    for k in cnt_lst:
        if k == K:
            cnt += 1
    print(cnt)










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


