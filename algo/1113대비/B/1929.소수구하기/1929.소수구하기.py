import sys
sys.stdin = open('input.txt')

M, N = map(int,input().split())

so_su = []  # 소수인 수를 받을 빈 리스트 만들기

for num in range(M, N+1):
    if M < 2 :  # 1은 소수가 아니므로 제외시키는 조건문 달아주기
        continue

    for i in range(2, num):
        if num%i == 0:  # 나누어 떨어지는 수가 있으면 소수 아님
            break
    else:
        so_su.append(num)

print(*so_su, sep='\n')