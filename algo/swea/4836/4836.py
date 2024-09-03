import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arrs = [list(map(int,input().split())) for _ in range(N)]

    # print(arrs)

    new = [[0]*10 for _ in range(10)]

    cnt = 0
    for a in range(N):
        r1 = arrs[a][0]
        c1 = arrs[a][1]
        r2 = arrs[a][2]
        c2 = arrs[a][3]


        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                new[i][j] += 1

                if new[i][j] == 2:
                    cnt += 1

    # for i in range(10):
    #     print(new[i])

    print(f'#{tc} {cnt}')
