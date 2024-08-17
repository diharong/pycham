import sys
sys.stdin = open('input.txt')

# 백준 - 2567. 색종이2

N = int(input()) # 색종이 수
arr = [[0]*102 for _ in range(102)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

result = 0 # 둘레값

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]  # 4뱡향 검사

for i in range(1,101):
    for j in range(1,101):
        if arr[i][j] == 1:
            for k in range(len(dx)):
                nx = i + dx[k]
                ny = j + dy[k]
                if arr[nx][ny] == 0:
                    result += 1

print(result)



