import sys
sys.stdin = open('input.txt')

N = int(input()) # 색종이의 수
arr = [[0]*101 for _ in range(101)]
for _ in range(N):
    # 해당 영역을 1로 표시
    x, y = map(int,input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

    # 1의 개수를 카운트 cnt = 넓이
    result = 0
    for i in arr:
        result += sum(i)

print(result)
