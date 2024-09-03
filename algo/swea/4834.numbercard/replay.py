import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input()))  # N개의 숫자

    cnt_li = [0] * 10

    for i in arr:
        cnt_li[i] += 1

    max_value = 0
    max_cnt = 0

    for j in range(1, 10):
