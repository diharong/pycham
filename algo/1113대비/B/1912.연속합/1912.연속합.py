# 백준 1912 연속합

import sys
sys.stdin = open('input.txt')

# 백준에서 오답 뜸
N = int(input())
arr = list(map(int,input().split()))

prefix = [0 for _ in range(N+1)]

for i in range(N):
    prefix[i+1] = max(prefix[i] + arr[i], arr[i])
    # 현재 수 가 누적합을 한 수보다 더 크다면 현재 수로 갱신

print(max(prefix))

# 지피티코드
# N = int(input())
# arr = list(map(int, input().split()))
#
# for i in range(1, N):
#     arr[i] = max(arr[i], arr[i] + arr[i - 1])
#
# print(max(arr))

