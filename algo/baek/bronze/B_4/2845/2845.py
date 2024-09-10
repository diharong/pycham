# 백준 2845 파티가 끝나고 난 뒤

import sys
sys.stdin = open('input.txt')

L, P = list(map(int,input().split()))   # L 사람수 P 파티 열렸던 곳 넓이
person = list(map(int,input().split()))

for i in person:
   print(i- L*P, end=' ')


# 런타임에러 망할
