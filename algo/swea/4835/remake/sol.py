import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split()) # N = 배열의 길이, M = 제약조건
    arr = [list(map(int, input().split())) for _ in range(N)]
    # li = list(zip(*arr))
    # print(li)
    # # for p in zip(*arr):
    # #
    # #     P = list(p)
    # #     # print(P)
    # '''열방향 도란'''
    #
    # # for i in range()

    