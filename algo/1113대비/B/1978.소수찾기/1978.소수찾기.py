import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int,input().split()))

not_sosu = 0    # 소수가 아닌 수를 셀 변수

for i in arr:   # 입력받은 리스트를 순회하며 하나씩 확인
    if i == 1:  # 1은 소수가 아님. 따라서 1일 땐 무시
        not_sosu += 1    # 소수가 아니므로 카운팅
        continue
    for j in range(2, i):   # 2부터 자기자신의 수 전까지 순회를 돌면서 소수 판별
        if i % j == 0:  # 나머지가 0이면 소수가 아니다.
            not_sosu += 1   # 카운팅
            break   # 중복 카운팅 방지

print(len(arr) - not_sosu)