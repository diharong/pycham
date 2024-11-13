import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    puzzle = [list(map(int,input().split())) for _ in range(N)]


    r_cnt = 0
    ans = 0

    # 행을 순회
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 1:
                r_cnt += 1
            else:
                if r_cnt == K:
                    ans += 1
                r_cnt = 0
        if r_cnt == K:
            ans += 1
        r_cnt = 0

    c_cnt = 0
    for j in range(N):
        for i in range(N):
            if puzzle[i][j] == 1:
                c_cnt += 1
            else:
                if c_cnt == K:
                    ans += 1
                c_cnt = 0
        if c_cnt == K:
            ans += 1
        c_cnt = 0

    print(f'#{tc}', ans)

