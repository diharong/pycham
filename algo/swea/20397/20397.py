import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N 돌의 수  M 뒤집기 횟수
    arr = list(map(int, input().split()))
    i, j = map(int, input().split())    # i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해
                                        # 각각 같은 색이면 뒤집고, 다른 색이면 그대로 둔다.



    for center in range(1, N-2):
        left = center - 1
        right = center + 1
        current = arr[center]

        while 0 <= left and right < N and arr[left] == arr[right]:
            if arr[left] == 1:
                arr[left] = 0
                arr[right] = 0


            else:
                arr[left], arr[right] = 1, 1

        print(arr)








