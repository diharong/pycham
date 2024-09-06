import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [input() for _ in range(N)]
    # print(arr)

    min_value = 123456789           # 충분히 큰 값으로 설정해야 함.

    w_cnt = 0
    for w in range(0, N-2):
        for j in range(M):
            if arr[w][j] != 'W':
                w_cnt += 1

        b_cnt = 0
        for b in range(w+1, N-1):
            for j in range(M):
                if arr[b][j] != 'B':
                    b_cnt += 1

            r_cnt = 0
            for r in range(b+1, N):
                for j in range(M):
                    if arr[r][j] != 'R':
                        r_cnt += 1


            s = w_cnt + b_cnt + r_cnt
            if min_value > s:
                min_value = s


    print(f'#{tc} {min_value}')








