# 1반 솔빙클럽 switch 문제

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())        # 스위치 개수
    Ai = list(map(int,input().split()))     # 조작 전
    Bi = list(map(int,input().split()))     # 조작 후


    # for i in range(N):
    #     if Ai[i] == Bi[i]:
    #         if i+1 < N:
    #             if Ai[i+1] == 0:
    #                 Ai[i+1] = 1
    #             elif Ai[i+1] == 1:
    #                 Ai[i+1] = 0

    # print(Ai)


    cnt = 0
    for i in range(N):
        while True:
            if Ai[i] != Bi[i]:
                for j in range(i, N):
                    if Ai[j] == 0:
                        Ai[j] = 1
                    elif Ai[j] == 1:
                        Ai[j] = 0
                cnt += 1

            else:
                break

    print(f'#{tc} {cnt}')



