import sys
sys.stdin = open('input.txt')

# 필요한 감독관 수의 최솟값을 구하는 프로그램 작성

N = int(input())    # 시험장 개수
Ai = list(map(int,input().split())) # 각 시험장에 있는 응시자 수
B, C = map(int,input().split()) # 총감독관 감시할 수 있는 응시자수 B, 부감독관 감시가능 수 C

# 총감독관은 반드시 1명 필요

# print(Ai)
result = 1



