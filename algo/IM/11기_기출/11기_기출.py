import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M1, M2 = map(int,input().split())
    arr = list(map(int,input().split()))

    arr.sort(reverse=True)

    M_1 = [i for i in range(1, M1+1)]
    M_2 = [i for i in range(1, M2 + 1)]
    M_s = M_1 + M_2

    M_s.sort()

    result = 0
    for i in range(N):
        result += M_s[i]*arr[i]

    print(f'#{tc} {result}')



