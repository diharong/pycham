import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M1, M2 = map(int,input().split())
    arr = list(map(int,input().split()))

    arr.sort()

    print(arr)

    M1_li = []  # 블록개수적은리스트
    M2_li = []  # 블록개수많은리스트

    if M1 < M2:
        M1_li.append(arr[-M1])
        M2_li.append(arr[-1])

    elif M1 > M2:
        M1_li.append(arr[-M1])
        M2_li.append(arr[-1])


    print(M1_li)
    print(M2_li)
