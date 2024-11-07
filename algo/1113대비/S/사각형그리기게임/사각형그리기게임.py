import sys
sys.stdin = open('input.txt')



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    rect_lst = []
    for i in range(N):
        for j in range(N):
            for k in range(i, N):
                for l in range(j, N):
                    if arr[i][j] == arr[k][l]:
                        rect = (k - i + 1) * (l - j + 1)
                        # 두개의 좌표가 같으면 0이 되기 때문에 +1
                        rect_lst.append(rect)

    max_v = max(rect_lst)
    count_v = rect_lst.count(max_v)
    print(f'#{tc} {count_v}')
#
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#
#
#
#
#     result = []
#     for i in range(N):
#         for j in range(N):
#             cnt = 0
#             for k in range(i, N):
#                 for z in range(j, N):
#                     if arr[i][j] ==
#











