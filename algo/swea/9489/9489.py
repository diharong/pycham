import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    max_value = 0
    ga_cnt = 0  # 가로찾기
    for i in range(N):
        for j in range(M-1):
            while True:
                if arr[i][j] == 1 and arr[i][j+1] == 1:
                    ga_cnt += 1
                else:
                    break

            if max_value < ga_cnt:
                max_value = ga_cnt


    s_cnt = 0
    for j in range(M):
        for i in range(N-1):
            while True:
                if arr[i][j] == 1 and arr[i+1][j] == 1:
                    s_cnt += 1
                else:
                    break

            if max_value < s_cnt:
                max_value = s_cnt



    print(max_value)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    result = []
    max_value = 0
    ga_cnt = 0  # 가로찾기

    for i in range(N):
        for j in range(M-1):
            if arr[i][j] == 1 and arr[i][j+1] == 1:
                ga_cnt += 1
            else:
                ga_cnt = 0

        if max_value < ga_cnt:
            max_value = ga_cnt
            result.append(max_value)


    s_cnt = 0

    for j in range(M):
        for i in range(N-1):

            if arr[i][j] == 1 and arr[i+1][j] == 1:
                s_cnt += 1
            else:
                s_cnt = 0

        if max_value < s_cnt:
            max_value = s_cnt
            result.append(max_value)

    print(max(result))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    max_value = 0

    for i in range(N):
        ga_cnt = 0  # 가로찾기
        for j in range(M):
            if arr[i][j] == 1 :
                ga_cnt += 1
                if max_value < ga_cnt:
                    max_value = ga_cnt
            else:
                ga_cnt = 0


    for j in range(M):
        s_cnt = 0
        for i in range(N):
            if arr[i][j] == 1 :
                s_cnt += 1
                if max_value < s_cnt:
                    max_value = s_cnt

            else:
                s_cnt = 0

    print(f'#{tc} {max_value}')