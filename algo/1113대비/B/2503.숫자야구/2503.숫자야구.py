# 백준 2503. 숫자야구
import sys
sys.stdin = open("input.txt")

# 영수가 정답으로 생각할 수 있는 모든 수를 넣어보기
# 그리고 B가 도전한 내용에 맞는지 확인하기!

N = int(input())

hint = [list(map(int,input().split())) for _ in rnage(4)]
# [[123,1,1], [356,1,0], ... ]

for a in range(1, 10): #100의 자리수
    for b in range(10): # 10의 자리수
        for c in range(10): # 1의 자리수

            if (a == b or b == c or c == a): # 같으면 숫자야구게임을 못하기때문에 조건걸어주고
                continue

            # 숫자가 정해졌다면
            for arr in hint:
                number = hint[0]
                strike = hint[1]
                ball = hint[2]

                # a,b,c 라는 숫자를
                # number 과 비교해서

                # 자리수를 나눠서, strike ball을 측정하는 부분
                for i in str(number):
                    pass


