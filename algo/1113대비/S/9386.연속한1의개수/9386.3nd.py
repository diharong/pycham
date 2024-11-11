import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().strip()))

    cnt = 0     # 1의 개수
    ans = 0     # 연속한 1의 개수

    for i in range(N):
        if arr[i] == 1:
            cnt += 1
            ans = max(cnt, ans)
        else:
            if cnt > 1:
                ans = max(cnt, ans)
            cnt = 0
    if cnt > 0:
        # ans = cnt 이게 아니고
        ans = max(cnt, ans) # 이렇게 비교해줘야함!

    print(f'#{tc}', ans)