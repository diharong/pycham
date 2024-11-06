import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

#행의 합
    s_li = []
    for i in range(100):
        cnt = 0
        for j in range(100):
            cnt+=arr[i][j]

        s_li.append(cnt)
    max_value1 = max(s_li)

    #열의 합
    s_li2 = []
    for j in range(100):
        cnt = 0
        for i in range(100):
            cnt += arr[i][j]

        s_li2.append((cnt))
    max_value2 = max(s_li2)

    # 대각선 왼쪽위
    s_li3 = []

    for i in range(100):
        cnt = 0
        for j in range(100):
            if i == j:
                cnt += arr[i][j]

        s_li3.append(cnt)
    max_value3 = sum(s_li3)



    # 대각선 오른쪽위
    s_li4 = []
    for i in range(100):
        cnt = 0
        for j in range(100):
            if i == abs(99-j):
                cnt += arr[i][j]

        s_li4.append(cnt)
    max_value4 = sum(s_li4)

    result = max(max_value1,max_value2,max_value3,max_value4)

    print(f'#{tc}', result)