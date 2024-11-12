import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    sample = list(map(int,input().split()))
    passcode = list(map(int,input().split()))

    check = []
    start = 0
    for i in range(K):
        for j in range(N):
            if sample[j] == passcode[i]:
                check.append(passcode[i])


    print(check)