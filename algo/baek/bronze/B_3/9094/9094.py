import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T+1):
#     n, m = map(int,input().split())
#
#     cnt = 0
#     for a,b in range(1, n+1):
#         if (a**2 + b**2 + m) % (a*b) == 0:
#             cnt += 1
#     print(cnt)

    '''진짜 ,,순서쌍이라고 했을 때 for문 두번 돌리는거 
    생각했었어야지.'''
T = int(input())
for tc in range(1, T+1):
    n, m = map(int,input().split())

    cnt = 0
    for a in range(1, n+1):
        for b in range(a+1, n):     # 이 범위도 조심하기

            if (a**2 + b**2 + m) % (a*b) == 0:
                cnt += 1
    print(cnt)