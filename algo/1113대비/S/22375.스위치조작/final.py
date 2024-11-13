import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Ai = list(map(int,input().split()))
    Bi = list(map(int,input().split()))

    if Ai == Bi:
        break

    cnt = 0  # 조작 횟수
    for i in range(N):
        if Ai[i] == Bi[i]:
            continue
        else:
            cnt += 1
            for j in range(i,N):
                Ai[j] = 1 - Ai[j]
            i = i+1

    print(f'#{tc}', cnt)