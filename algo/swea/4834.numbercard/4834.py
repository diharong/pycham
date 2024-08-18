import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    cnt_lst = [0]*10        # 0~9까지 숫자의 빈도 수를 저장할 리스트

    for i in arr:           # 각 숫자의 빈도를 카운트
        cnt_lst[i] += 1

    # 가장 많이 등장한 숫자와 그 빈도 찾기
    max_cnt = 0
    max_num = 0


    for i in range(len(cnt_lst)):
        if max_cnt < cnt_lst[i] or (cnt_lst[i] == max_cnt and i > max_num):
            max_cnt = cnt_lst[i]
            max_num = i

    print(f'#{tc} {max_num} {max_cnt}')
