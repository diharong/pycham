import sys
sys.stdin = open('input.txt')

N = int(input())    # NXN
arr = [list(map(int,input().split())) for _ in range(N)]
K = int(input())    # 마법사의 시전범위

# 대각선
dx = [1,1,-1,-1]
dy = [-1,1,1,-1]

max_monster = 0
for i in range(N):
    for j in range(N):
        S = 0

        # 대각선 4방향 탐색
        for h in range(4):
            for z in range(1, K+1):
                nx = i + dx[h]*z
                ny = j + dy[h]*z
                if 0 <= nx < N and 0 <= ny < N:
                    S += arr[nx][ny]

            if max_monster < S:
                max_monster = S

print(max_monster)

