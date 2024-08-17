import sys
sys.stdin = open('input.txt')

N = int(input())

result = 0
for i in range(1,N+1):
    for j in range(i, N+1):
        if i*j <= N:
            result += 1

print(result)