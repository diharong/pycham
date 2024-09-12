from collections import deque

import sys
sys.stdin = open('input.txt')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    global result
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) == (end_x - 1, end_y - 1):
                result = 1
            if 0 <= nx < 100 and 0 <= ny < 100 and miro[nx][ny] == 0:
                q.append((nx, ny))
                miro[nx][ny] = miro[x][y] + 1

    return result


for _ in range(10):
    result = 0
    T = int(input())
    miro = [list(map(int, input())) for i in range(100)]
    for x in range(100):
        for y in range(100):
            if miro[x][y] == 2:
                start_x, start_y = x, y
            if miro[x][y] == 3:
                end_x, end_y = x, y


    bfs(start_x, start_y)
    print(f'#{T} {result}')