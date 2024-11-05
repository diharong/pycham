import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int,input()))
#
#     cnt = 0     # 1을 카운트할 변수
#     for i in range(len(arr)):
#         if arr[i] == 1:     # 만약 인덱스 값이 1이면
#             cnt += 1    # cnt 변수에 1을 추가한다.
#
#         elif arr[i] == 0:   # 만약 인덱스 값이 0이라면
#             continue    # 넘어간다.
#
#     print(f'#{tc}', cnt)

'''
이렇게 짜니까 뒤에 0이 나와도 1이 계속 더해진다. 
0이 나오면 cnt가 0으로 초기화되어야한다.

그걸 어떻게 ,, ? 

음, 우선 cnt 한 수를 모으는 ? 리스트를 만들어서 그 중에 최댓값을 출력하는 방법으로 바꿔본다.
'''


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input()))

    # print(arr)
    cnt_li = []     # cnt 한 값들을 넣어줄 빈 리스트
    cnt = 0

    for i in range(len(arr)):

        if arr[i] == 1:     # 만약 인덱스 값이 1이면
            cnt += 1    # cnt 변수에 1을 증가시키고
            cnt_li.append(cnt)  # 그 값을 cnt_li에 넣는다.
            if arr[i+1] == 0:   # 만약 다음 인덱스 값이 0이 나오면
                cnt = 0     # 카운트 값을 초기화 시킨다.

        elif arr[i] == 0:
            continue

    print(f'#{tc}', max(cnt_li))

'''
이렇게 하고 출력하니까 인덱스 에러가 났다.
나는 계속 인덱스 에러장인이다. ;; 

어디서 인덱스 에러가 나는지 보니까 
if arr[i+1] == 0: 여기이다. 
당연한것을,, ? 그래서 len(arr)+1 로 설정했더니
if arr[i] == 1 : 에서 인덱스 에러가 났다.

다시 생각해보자 . 음 그럼 
i+1 범위의 조건을 다시 추가해주면 되지 않을까 ?
i+1 이 N을 넘지 않는다는 조건을 추가해보자!
'''


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input()))

    cnt_li = []
    cnt = 0
    for i in range(len(arr)):

        if arr[i] == 1:
            cnt += 1
            cnt_li.append(cnt)
            if i+1 < N: # 조건 추가
                if arr[i+1] == 0:
                    cnt = 0

        elif arr[i] == 0:
            continue

    print(f'#{tc}', max(cnt_li))


'''
정답 나옴! 
근데 print(cnt_li) 를 하니까 
#1 [1, 2, 1, 2, 3]
#2 [1, 1]
#3 [1, 2, 3, 1, 2, 3, 4]
이렇게 담기더라

이렇게 도출해내는게 맞는지,,의문

더 좋은 방법은 없을까!?

못풀줄알았는데 그래도 풀렸다 휴 ㅠ
'''