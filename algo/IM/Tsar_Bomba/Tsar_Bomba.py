# 차르봄바

import sys
sys.stdin = open("input.txt")

T = int(input())    # 테스트케이스수를 입력받음
for tc in range(1, T+1):    # 테케만큼 순회할꺼
    N, P = map(int,input().split()) # N: 마을크기, P : 차르파워
    virus_arr = [list(map(int,input().split()))for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_value = 0       # 제거된 최대 바이러스 수값 변수 & 초기화

    for virus_i in range(N):    # virus_arr 를 전체 순회
        for virus_j in range(N):
            current_sum = virus_arr[virus_i][virus_j]
            for k in range(4):      # 4방향 탐색
                for p in range(1, P+1):   # 차르파워만큼 퍼지고, 그 값들을 더해야한다
                    ni = virus_i + di[k]*p
                    nj = virus_j + dj[k]*p
                    if 0 <= ni < N and 0 <= nj < N:
                        current_sum += virus_arr[ni][nj]

            if max_value < current_sum:
                max_value = current_sum


    print(f'#{tc} {max_value}')