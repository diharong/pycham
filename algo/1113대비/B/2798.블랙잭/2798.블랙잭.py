# 백준 2798. 블랙잭
import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())
num_li = list(map(int,input().split()))

max_value = 0 # 최대합 초기값설정
S = 0
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if num_li[i]+num_li[j]+num_li[k] <= M:
                S = num_li[i]+num_li[j]+num_li[k]

            if max_value < S:
                max_value = S

print(max_value)



# max_value = 0 # 최대합 초기값설정
# S = 0
# for i in range(0, N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             if max_value < num_li[i]+num_li[j]+num_li[k] <= M:
#                    max_value = num_li[i]+num_li[j]+num_li[k]
#
#
# print(max_value)