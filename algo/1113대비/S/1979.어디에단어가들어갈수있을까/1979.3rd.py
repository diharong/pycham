# 어디에 단어가 들어갈 수 있을까

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = 0    # K 길이와 일치하는 단어의 개수(결과값)를 도출할 변수

    # 행 순회
    for i in range(N):
        r_cnt = 0   # 행 순회 시 발견한 단어의 개수를 담을 변수
        for j in range(N):
            if arr[i][j] == 1:  # 배열 순회 시 1을 만났을 때
                r_cnt += 1  # 변수에 1을 담아준다.

            else:   # arr[i][j]==0  # 배열 순회시 1을 아닌 수 즉, 0을 만났을 때
                # 만약 이전에 r_cnt 값이 존재하고, 그 값이 K와 동일한 값이라면
                # K 길이와 일치하는 단어를 발견한 것이므로
                if r_cnt == K:
                    ans += 1    # ans 값을 1 증가시켜준다.
                # 배열 순회시 0을 만났을 때는 연속된 단어를 담을 수 없으므로
                # 변수를 0으로 초기화 시켜주고, 다음 인덱스 값을 확인한다.
                r_cnt = 0
        # 한 열의 순회가 끝났을 때 위에서 조건으로 처리하지 못한 조건을 처리해주어야한다.
        # 즉, 배열이 1로 종료되었을 경우, r_cnt 값을 K값과 비교하여 동일하다면
        # 결과 변수값에 1을 증가시켜야한다.
        if r_cnt == K:
            ans += 1

    # 열 순회
    for j in range(N):
        c_cnt = 0   # 열 순회 시 발견한 단어의 개수를 담을 변수
        for i in range(N):
            if arr[i][j] == 1:
                c_cnt += 1

            else:   # arr[i][j]==0
                if c_cnt == K:
                    ans += 1
                c_cnt = 0

        if c_cnt == K:
            ans += 1

    print(f'#{tc}', ans)


