import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Ai = list(map(int,input().split()))
    Bi = list(map(int,input().split()))

    cnt = 0
    while True:
        if Ai == Bi:
            break

        for i in range(N):
            for j in range(i, N):
                if Ai[j] == 1:
                    Ai[j] = 0
                    cnt += 1
                elif Ai[j] == 0:
                    Ai[j] = 1
                    cnt += 1
        break

    print(cnt)

    #2번째
    # cnt = 0
    # while True:
    #     if Ai == Bi:
    #         break
    #
    #     for i in range(N):
    #         if Ai[i] == Bi[i]:
    #             continue
    #
    #         else:
    #             for j in range(i, N):
    #                 if Ai[j] == 1:
    #                     Ai[j] = 0
    #                     cnt += 1
    #                 elif Ai[j] == 0:
    #                     Ai[j] = 1
    #                     cnt += 1
    #             break
    #
    # print(cnt)



    #1번째째
    # cnt = 0
   # while True:
    #     if Ai == Bi:
    #         break
    #
    #     for i in range(N):
    #         if Ai[i] == Bi[i]:
    #             continue
    #
    #         elif Ai[i] != Bi[i]:
    #             for j in range(i, N):
    #                 if Ai[j] == 1:
    #                     Ai[j] = 0
    #                     cnt += 1
    #                 elif Ai[j] == 0:
    #                     Ai[j] = 1
    #                     cnt += 1
    #                 break
    #
    # print(cnt)





'''

출력값
#1 2
#2 1
#3 3

while문에서 바로print로 넘어가는 대참사 ;; 

'''

'''
음 뒤에 까지 어케 바꿈,, ? i번째부터 N번까지..
지금은 해당 인덱스만 바뀜
'''



