import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M1, M2 = map(int, input().split())
    block = list(map(int, input().split()))
    block.sort()
    M1_lst = []
    M2_lst = []
    for i in range(min(M1, M2)):
        M1_lst.append(block.pop())
        M2_lst.append(block.pop())
    for j in range(abs(M1 - M2)):
        if M1 > M2:
            M1_lst.append(block.pop())
        else:
            M2_lst.append(block.pop())
    M1_lst.sort(reverse=True)
    M2_lst.sort(reverse=True)
    sum_v = []
    for k in range(len(M1_lst)):
        sum_v.append((k + 1) * M1_lst[k])
    for l in range(len(M2_lst)):
        sum_v.append((l + 1) * M2_lst[l])
    result = sum(sum_v)

    print(f'#{tc} {result}')