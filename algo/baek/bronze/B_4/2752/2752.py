# 세수정렬

import sys
sys.stdin = open('input.txt', 'r')

arr = list(map(int,input().split()))

# print(arr)

arr.sort()

print(*arr)