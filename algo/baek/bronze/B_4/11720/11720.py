# 백준 11720 숫자의 합

import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(input())

# print(arr)

result = 0
for i in arr:
    result += int(i)

print(result)



