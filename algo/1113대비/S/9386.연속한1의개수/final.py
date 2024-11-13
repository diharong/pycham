import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().strip()))

    cnt =0 # 1의 개수를 담을 변수
    max_value = 0   # 연속한 1의 최대값을 받을 변수
    for i in range(N):
        if arr[i] == 1:
            cnt += 1
            max_value = max(cnt, max_value)

        else:
            if cnt > 0: # 만약 0이전에 1이 존재했다면
                max_value = max(cnt, max_value) # 최대값이랑 비교해서 갱신

            cnt = 0

    if cnt > 0:
        max_value = max(cnt, max_value)
        cnt = 0

    print(f'#{tc}', max_value)