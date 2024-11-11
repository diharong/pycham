import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, 11):
    N = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]











    # # 하,우,좌 방향탐색
    # dx = [0, 1, -1]
    # dy = [1, 0, 0]
    #
    # x_point = []    # x좌표값
    #
    # for i in range(100):
    #     for j in range(100):
    #         current = ladder[i][j]
    #
    #         if ladder[i][j] == 1:
    #
    #             for k in range(3):
    #                 ni = i + dx[k]
    #                 nj = j + dy[k]
    #
    #                 if 0 <= ni < 100 and 0 <= nj < 100:
    #                     while ladder[ni][nj] != 0:
    #                         current = ladder[ni][nj]
    #                         if ladder[ni][nj] == 0:
    #                             break
    #
    # print(current)



    # for i in range(100):
    #     for j in range(100):
    #         # 현재위치
    #         current = ladder[i][j]
    #
    #         # 만약에 1을 발견하면
    #         if ladder[i][j] == 1:
    #             # 방향탐색을 시작하여 1을 찾는다.
    #             x_point.append(i)
    #             for k in range(3):
    #                 ni = i + dx[k]
    #                 nj = j + dy[k]
    #                 if 0 <= ni < 100 and 0 <= nj <100:
    #                     if ladder[ni][nj] == 1:
    #                         current = ladder[ni][nj]
    #                     elif ladder[ni][nj] == 0:
    #                         continue
    #
    #         elif ladder[i][j] == 0:
    #             continue
    #
    #         elif ladder[i][j] == 2:
    #             x_point = x_point[0]
    #             break
    # print(x_point)


