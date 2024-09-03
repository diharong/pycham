import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int,input().split())
    arr = list(map(int,input().split()))    # 충천기 있는 정류장 번호

    for i in range(N+1):
        if 
