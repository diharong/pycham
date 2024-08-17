import sys
sys.stdin = open('input.txt')


x, y = map(int, input().split())
cut = int(input())
# arr = [False for _ in range(N)] 이렇게 하는거 아님

ga = [x,0]
se = [0,y]


for _ in range(cut):
    n, m = map(int, input().split())

    if n == 0:
        se.append(m)
    else:
        ga.append(m)

ga = sorted(ga)
se = sorted(se)
result = []

'''
밑에 for 문 1부터 순회하는 이유 : 현재 경계와 '이전' 경계사이의 거리를 계산하기위해
인덱스가 [0] 부터 시작하면 이전 인덱스가 존재하지 않기 때문에 
현재 인덱스를 [1]로 잡아준다.
'''
for i in range(1, len(ga)):
    for j in range(1, len(se)):
        w = ga[i]-ga[i-1]
        h = se[j]-se[j-1]
        result.append(w*h)

print(max(result))





