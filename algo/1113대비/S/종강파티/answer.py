# 종강파티
import sys
sys.stdin = open('input.txt')

from math import ceil

N, M = map(int, input().split())
six_lst = []
one_lst = []
for i in range(M):
    six, one = map(int, input().split())
    six_lst.append(six)
    one_lst.append(one)

min_lst = [min(six_lst), min(one_lst)]
min_v = 0
if N % 6 == 0:
    min_v = min(min_lst[0] * (N // 6), min_lst[1] * N)
else:
    min_v = min(ceil(N / 6) * min_lst[0], min_lst[1] * N, (min_lst[0] * (N // 6)) + (min_lst[1] * (N % 6)))
print(min_v)