import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]


    min_value = 1000000000000000
    for i in range(N):
        for j in range(N):
            S = arr[i][j]
            if 0 <= j+1 < N and 0 <= i+1 < N:
                S += min(arr[i][j+1], arr[i+1][j])

        if min_value > S:
            min_value = S

    print(min_value)