import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M1, M2 = map(int,input().split())
    weight = list(map(int,input().split()))

    # print(N, M1, M2)
    # print(weight)

    weight.sort()
    M1_lst = []
    M2_lst = []

    print(weight)
