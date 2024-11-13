import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    lst = []
    for i in range(N):
        for j in range(N):
            for k in range(i+1, N):
                for z in range(j, N):
                    if arr[i][j] == arr[k][z]:
                        box = (k-i+1) * (z-j+1)
                        lst.append(box)

    max_value = max(lst)

    count_v = lst.count(max_value)
    print(f'#{tc}', count_v)


