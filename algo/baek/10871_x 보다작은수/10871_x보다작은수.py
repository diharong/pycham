import sys
sys.stdin = open('input.txt', 'r')

N, X = map(int, input().split())

arr = list(map(int, input().split()))

# print(arr)

for i in range(N):
    if arr[i] < X:
        print(arr[i], end=' ')