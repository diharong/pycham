import sys
sys.stdin = open('input.txt')


N = int(input())
switch = list(map(int,input().split()))
student = int(input())

for _ in range(student):
    S, GN = map(int, input().split()) # 성별(S), 받은 수(GN)

    if S == 1:      # 남학생일 때
        pass