import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    max_value = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            S = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    S += arr[k][l]

            if max_value < S:
                max_value = S

    print(max_value)
