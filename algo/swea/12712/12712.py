import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N 배열 M 세기
    arr = [list(map(int, input().split())) for _ in range(N)]


    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_value = 0

    for i in range(N):
        for j in range(N):
            S = arr[i][j]
            for k in range(1, N-1):
                for l in range(1, k+1):
                    ni = i+di[k]*l
                    nj = j+dj[k]*l
                    if 0 <= ni < N and 0 <= nj < N:
                        S += arr[i][j] + arr[ni][nj]

            if max_value < S:
                max_value = S


    print(max_value)
