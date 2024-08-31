import sys
sys.stdin = open('input.txt')

N, K = map(int,input().split())

'''N의 약수중 K번째로 작은수 출력'''
'''6의 약수중 3번째로 작은수 
    25의 약수중 4번째로 작은수'''

# result = []
#
# for i in range(1,N+1):
#     if N%i == 0:
#         result.append(i)
#
# # result.sort()
# # print(result[K-1])

'''이렇게 하니까 런타임에러 남 '''

result = []

for i in range(1,N+1):
    if N%i == 0:
        result.append(i)

if K > len(result):
    print(0)
else :
    print(result[K-1])







