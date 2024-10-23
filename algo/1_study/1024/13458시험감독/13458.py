import sys
sys.stdin = open('input.txt')

# 필요한 감독관 수의 최솟값을 구하는 프로그램 작성

N = int(input())    # 시험장 개수
Ai = list(map(int,input().split())) # 각 시험장에 있는 응시자 수
B, C = map(int,input().split()) # 총감독관 감시할 수 있는 응시자수 B, 부감독관 감시가능 수 C

# 총감독관은 반드시 1명 필요

# # print(Ai)
# cnt = N

# for i in N:
#     temp = (Ai - B)
#     if temp > 0:
#         if temp <= C :
#             if temp%C == 0 or 0 < temp%C < temp:

#                 cnt += 1
            
        
#     result.append(cnt)

    
# print(result)

cnt = N 
for i in Ai:
    i -= B
    if i > 0:
        if i % C:
            cnt += (i//C) +1
        else:
            cnt += i//C

print(cnt)