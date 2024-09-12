import sys
sys.stdin = open('input.txt')










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


