import sys
sys.stdin = open('input.txt')
import math

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N+1)]

    house = []
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] == 2:
                repeater = (i,j)
            elif arr[i][j] == 1:
                house.append((i,j))

    dist = []
    for hx, hy in house:
        length = math.sqrt(((hy-repeater[1])**2) + ((hx-repeater[0])**2))
        # length = math.sqrt(((repeater[1]-hy)**2) + ((repeater[0]-hx)**2))

        # dist.append(length)
        dist.append(math.ceil(length))
    result = max(dist)
    print(f'#{tc}', result)



