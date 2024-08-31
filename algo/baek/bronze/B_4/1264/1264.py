import sys
sys.stdin = open('input.txt')


'''
모음의 개수
a, e, i, o, u
'''

# li = list(map(str, input().split()))
# print(li)
#
# cnt = 0
# for i in range(len(li)):
#     if 'a' or 'e' or 'i' or 'o' or 'u' in li[i]:
#         cnt += 1
#
# print(cnt)
#

while True:
    Li = input()
    cnt = 0
    if Li == '#':
        break
    else:
        for i in Li:
            if i in 'aeiouAEIOU':
                cnt += 1
        print(cnt)

