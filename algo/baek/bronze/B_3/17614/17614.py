import sys
sys.stdin = open('input.txt')

# N = int(input())

# cnt = 0
# for i in range(1, N+1):
#     if i in 369:
#         cnt += 1
#
# print(cnt)

'''오류'''
N = int(input())

cnt = 0
for num in range(1, N+1):
    for i in str(num):
        if i == '3' or i =='6' or i == '9':
            cnt += 1
print(cnt)