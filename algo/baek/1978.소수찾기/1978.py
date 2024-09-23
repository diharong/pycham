import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(map(int,input().split()))

result = []
for i in arr:
    if i !=1:
        if i%i == 0:
            result.append(i)


print(len(result))




