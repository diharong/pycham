import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))


    start = [ 0 for _ in range(N)]  # 초기의 빈 배열 만들기

    if start == arr:    # 만약, 시작 값과 출력값이 같으면 종료한다.
        break

    cnt = 0

    for i in range(1, N+1):
        if start[i-1] == arr[i-1]:
            continue
        else:
            cnt += 1
            for j in range(i, N+1, i):
                start[j-1] = 1 - start[j-1]


    print(f'#{tc}', cnt)




    # cnt = 0
    # for i in range(1, N):
    #     if start[i] == arr[i]:
    #         continue
    #     elif start[i] != arr[i]:
    #         cnt += 1
    #         for j in range(i, N, i):
    #
    #             start[j] = 1 - start[j]
    #
    # print(cnt)