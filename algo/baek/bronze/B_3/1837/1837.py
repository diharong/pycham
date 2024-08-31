import sys
sys.stdin = open('input.txt')

P, K = map(int, input().split())

result = []
for i in range(2, K+1):
    if P%i == 0:
        result.append(i)
        if i < K:
            print('BAD', i)
            break           # break 왜 하는거야 ,..
else:
    print('GOOD')


# print(result)
