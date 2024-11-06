import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, P = map(int,input().split()) # N 마을의 크기, P 파워
    arr = [list(map(int,input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    max_value = 0

    for i in range(N):
        for j in range(N):
            S = arr[i][j]

            # 4방향 탐색
            for k in range(4):
                for z in range(1, P+1):
                    nx = i + dx[k]*z
                    ny = j + dy[k]*z

                    #범위 안에 있는지 확인
                    if 0 <= nx < N and 0 <= ny < N:
                        S += arr[nx][ny]

            if max_value < S:
                max_value = S


    print(f'#{tc}' , max_value)


