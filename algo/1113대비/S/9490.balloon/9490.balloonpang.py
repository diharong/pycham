import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    max_value = 0

    for i in range(N):
        for j in range(M):
            S = arr[i][j]

            for k in range(4):  # 4방향 탐색
                for z in range(1, arr[i][j]+1): # 왜 0부터 아님,,?
                    # 자기자신을 더하지 않기 위해서
                    nx = i + dx[k]*z
                    ny = j + dy[k]*z
                    if 0 <= nx < N and 0 <= ny < M:
                        S += arr[nx][ny]

            if max_value < S:
                max_value = S

    print(f'#{tc}', max_value)

'''
for z in range(1, arr[i][j]+1) 에서 

z는 현재 위치에서 지정된 거리만큼 떨어진 칸을 탐색하는 역할을 한다.
만약 range(0, arr[i][j])처럼 0부터 시작하면, 
z=0일 때 (nx, ny)가 현재 위치 (i, j)와 동일해집니다. 
이렇게 되면 이미 더해진 arr[i][j]가 또 더해져 잘못된 값이 나오게 됩니다.
따라서 range(1, arr[i][j]+1)로 설정하여 현재 위치는 제외하고, 
1칸부터 arr[i][j] 칸만큼 떨어진 칸들만 탐색하도록 하는 것입니다.
'''