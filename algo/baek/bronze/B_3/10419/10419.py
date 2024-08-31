import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    d = int(input())

    result = []
    for t in range(d+1):
        if t + (t**2) <= d:     # t + 를 생각못함
            result.append(t)

    print(max(result))
