import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int,input().split()))

    s = sum(arr)
    l = len(arr)

    result = round(s/l)

    print(f'#{tc} {result}')
