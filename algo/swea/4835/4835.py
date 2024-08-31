import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))

    # arr.sort()            # ??? 이걸 하니까 계속 답 안나옴 ;;;
    # print(arr)
    # min_v = sum(arr[:M])
    # max_v = sum(arr[:N-M-1:-1])
    # print(max_v - min_v)
    result = []
    for i in range(N-M+1):
        S = sum(arr[i:i+M])
        result.append(S)
    print(max(result)-min(result))





