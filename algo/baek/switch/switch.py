import sys
sys.stdin = open('input.txt')


N = int(input())    # 스위치 개수
switch = list(map(int, input().split()))    # 각 스위치 상태
student = int(input())      # 학생 수

for _ in range(student):
    S, GN = map(int, input().split())



    if S == 1:
        for i in range(1, N+1):
            if i%GN == 0:
                if switch[i-1] == 0:    # 왜 GN -1 이 아닐까요~ 단하나의 스위치만 제어하므로 !!!
                    switch[i-1] = 1
                else:
                    switch[i-1] = 0
    else:
        if switch[GN-1] == 0:
            switch[GN-1] =1
        else:
            switch[GN-1] = 0

            for k in range(1, N+1):
                if 0 <= GN-1-k and GN-1+k < N:
                    if switch[GN-1-k] == switch[GN-1+k]:
                        if switch[GN-1-k] == 1:
                            switch[GN-1-k] = 0
                            switch[GN-1+k] = 0
                        else:
                            switch[GN-1-k] = 1
                            switch[GN-1+k] = 1
                    else:
                        break
                else:
                    break

for i in range(N):
    print(switch[i], end=' ')
    if (i + 1) % 20 == 0:  # 20개씩 줄 바꿈                 # 이건 방식을 아예 몰랐다. 외워야겠다!
        print()