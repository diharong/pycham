# swea 9490. 풍선팡1

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_value = 0

    for i in range(N):
        for j in range(M):
            S = arr[i][j]
            for k in range(4):      # 4방향 탐색하기 위한 반복문
                for l in range(1, arr[i][j]+1):    # 칸 안의 수 (만큼 터질꺼임)
                    ni = i + di[k]*l
                    nj = j + dj[k]*l
                    if 0 <= ni < N and 0 <= nj < M:
                        S += arr[ni][nj]

            if max_value < S:
                max_value = S

    print(f'#{tc} {max_value}')


    '''
    for l in range(arr[i][j]+1):
    arr[i][j] + 1 하는 이유   
    : arr[i][j] 가 1 일 때 
    for l in range(1)
    l 의 범위는 0에서 멈춘다 
    1 까지 가려면 +1 해주야한다.   
    '''