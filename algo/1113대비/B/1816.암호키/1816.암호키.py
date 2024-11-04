import sys
sys.stdin = open('input.txt')

'''
1,000,000 보다 작고 2이상인 약수를 가지고 있다면, 틀린 비밀번호!
'''


N = int(input())
for _ in range(N):
    num = int(input())

    for i in range(2, 1_000_001):
        if num%i == 0:
            print("NO")
            break
    else:
        print("YES")


# N = int(input())
# for _ in range(N):
#     num = int(input())
#
#     for i in range(2, 1_000_001):
#         if num%i == 0:
#             print("NO")
#             break
#         if num%i !=0:
#             print("YES")
#             break
