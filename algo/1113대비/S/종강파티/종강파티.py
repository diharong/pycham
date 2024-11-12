# 그리디

import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split()) #N명, M개의 보드카
arr = [list(map(int,input().split())) for _ in range(M)]

# print(arr)

price = 0
for i in range(M):
    if N == arr[i][0]:
        price += arr[i][0]
        break
    else:
        pass
