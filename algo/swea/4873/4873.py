import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    st = list(str(input()))
    # print(st)

    stack = []
    for i in st:
        if len(stack) == 0:
            stack.append(i)

        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    print(f'#{tc} {len(stack)}')