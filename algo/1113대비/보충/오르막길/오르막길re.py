import sys
sys.stdin = open('input.txt')

N = int(input())
Pi = list(map(int,input().split()))


for i in range(1,N):
    if Pi[i]-Pi[i-1] > 0:

    else:
