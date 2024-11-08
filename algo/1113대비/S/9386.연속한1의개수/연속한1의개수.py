import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input()))

    stack = []
    cnt_lst = []
    for i in range(N):
        if arr[i] == 0:
            if len(stack) != 0:
                cnt_lst.append(len(stack))
            stack = []

        else:
            stack.append(1)

    if len(stack) != 0:
        cnt_lst.append(len(stack))

    print(f'#{tc}', max(cnt_lst))