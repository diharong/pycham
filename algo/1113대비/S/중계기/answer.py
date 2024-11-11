import sys
sys.stdin = open('input.txt')
import math
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N+1)]

    one_lst = []
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] == 2:
                mid = (i,j)
            elif arr[i][j] == 1:
                one_lst.append((i,j))
    distance = []
    for x,y in one_lst:
        length = math.sqrt(((mid[0]-x)**2) + ((mid[1]-y)**2))
        distance.append(math.ceil(length))
    result = max(distance)
    print(f'#{tc} {result}')
