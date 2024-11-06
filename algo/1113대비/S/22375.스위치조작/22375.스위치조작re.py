import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # N 스위치의 개수
    Ai = list(map(int,input().split()))
    Bi = list(map(int,input().split()))

    # print(Ai)
    cnt = 0     # 스위치 조작 횟수를 카운팅할 변수

    if Ai == Bi:    # 만약 Ai 와 Bi 의 상태가 같으면
        break       # 강제 종료한다.
    else:           # Ai 와 Bi 의 상태가 다를경우
        for i in range(N):  # Ai 의 배열을 순회하면서 인덱스값을 확인
            if Ai[i] == Bi[i]:  # 만약 둘의 인덱스 값이 같다면
                continue    # 다음 코드로 넘어간다.
            else:           # 만약 둘의 인덱스 값이 다르다면
                cnt += 1    # 스위치 상태를 변경 해야하므로 cnt 값을 증가시켜준다.
                for j in range(i,N):    # 배열을 순회하면서
                    Ai[j] = 1 - Ai[j]   # 스위치 상태를 바꿔준다.
                    # 여기서 cnt를 위치를 잘 설정해야하는데, 만약 for문안에서
                    # cnt 할 경우 인덱스 값이 변경 될 때마다 카운팅 된다.
                    # 하지만 문제에서는 한번 변경될때 N번째 스위치 까지 모두 변경되므로
                    # 변경 횟수만 카운팅 해준뒤
                    # for문 전체를 모두 순회하여 스위치 상태를 끝까지 바꿔줘야한다.

    print(f'#{tc}', cnt)

    ''' 이왜진~!!!?!?!?? '''

