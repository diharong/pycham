# 백준 수열 2559

import sys
sys.stdin = open("input.txt")

N, K = map(int,input().split())
arr = list(map(int,input().split()))

# result = []
# S = 0
# for i in range(0,9):
#     for j in range(i+1, 10):
#         S = arr[i]+arr[j]
#         result.append(S)
#
#
# print(result)


# prefix 누적합
prefix = [0 for _ in range(N+1)] # 1칸 더 크게 만들기

for i in range(N):
    prefix[i+1] = prefix[i] + arr[i]

answer = []
for j in range(K, N+1):
    answer.append(prefix[j]- prefix[j-K])

print(max(answer))