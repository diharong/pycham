import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split()) # N x N, K = 단어길이
    arr = [list(map(int,input().split())) for _ in range(N)]

    # print(N, K)

    padded_array = [[0]*(N+2) for _ in range(N+2)]

    for i in range(N):
        for j in range(N):
            padded_array[i+1][j+1] = arr[i][j]

    # print(padded_array)

