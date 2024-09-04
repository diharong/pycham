import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(str(input())) for _ in range(N)]

    current_value = []
    for i in range(N):
        for j in range(N):
            left = i - 1
            right = i + 1



            while 0 <= left and right < N and arr[left] == arr[right]:
                left -= 1
                right += 1





                print(current_value)
