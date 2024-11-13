import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    sample = list(map(int,input().split()))
    passcode = list(map(int,input().split()))

    result = []
    check = 0

    for i in range(K):
        for j in range(check, N):
            if passcode[i] == sample[j]:
                result.append(j)
                check = j+1
                break
    if len(result) == K:
        ans = 1
    else:
        ans = 0


    print(f'#{tc}', ans)




