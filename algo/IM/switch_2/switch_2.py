# 2반 솔빙 스위치 문제

import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())        # N 조명 수
    want = list(map(int,input().split()))


    start = [0]*N

    cnt = 0

    for i in range(1, N+1):       # 처음 상태 리스트 순회
        if start[i-1] != want[i-1]:
            for j in range(i, N+1, i):
                start[j-1] = 1 - start[j-1]
            cnt += 1



    print(f'#{tc} {cnt}')


