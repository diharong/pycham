# 백준 2742. 기찍 N

import sys
sys.stdin = open('input.txt')

N = int(input())

for i in range(1, N+1):
    print(i)


# 1. 거꾸로 리스트를 만든다.
li = []
for i in range(1, N+1):
    li.append(i)
li.sort(reverse=True)
for i in range(len(li)):
    print(li[i])

# 2. 그냥 거꾸로 출력한다.
for i in range(N, 0, -1):
    print(i)