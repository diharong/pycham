# 백준 2562. 최댓값

import sys
sys.stdin = open('input.txt')

N_li = []

for _ in range(9):
    a = int(input())
    N_li.append(a)

# result = 0

print(max(N_li))
print(N_li.index(max(N_li))+1)





