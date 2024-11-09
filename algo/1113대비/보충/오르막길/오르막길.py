import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int,input().split()))

# 오르막길의 크기 = 마지막 숫자 - 첫 번째 숫자

road = []
for i in range(1, N):
    sub = arr[i] - arr[i-1]
    if sub > 0:
        pass



