import sys
sys.stdin = open('input.txt')

for tc in range(3):
    N = int(input())
    li = [int(input()) for i in range(N)]

    S = sum(li)
    if S == 0:
        print('0')
    elif S > 0:
        print('+')
    else:
        print('-')

'''시간초과나옴'''

# import sys
# input = sys.stdin.readline
#
# # 테스트케이스
# for _ in range(3):
#     # 입력
#     n = int(input())
#     _sum = 0
#
#     for _ in range(n):
#         _sum += int(input())
#
#     # 출력
#     if _sum == 0:
#         print(0)
#     elif _sum < 0:
#         print("-")
#     else:
#         print("+")






# for _ in range(3):
#     N = int(input())
#     li = [int(input()) for i in range(N)]
#
#     print(li)



