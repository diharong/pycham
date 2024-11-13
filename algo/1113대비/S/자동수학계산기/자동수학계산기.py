import sys
sys.stdin = open('input.txt')

num_list = list(input().strip())
print(num_list)

result = 0 # 결과값
num = ''    # 숫자를 저장할 문자열 변수
sign = 1    # 양수 음수 판별

# 입력이 숫자로 시작하는 경우에만 진행
if num_list[0].isdigit():
    for i in range(len(num_list)):
        # 현재 문자가 숫자일때
        if num_list[i].isdigit():
            # 숫자 문자열에 해당 숫자를 추가
            num += num_list[i]
        # 부호일때
        else:
            # num에 숫자가 있을 때, 누적 결과에 현재숫자(부호 포함)을 더함
            if num:
                result += sign*int(num) # 부호 적용 후 숫자 더하기
                num = ''    # num 초기화
            # 부호에 따라 sign 값을 설정
            if num_list[i] == '+':
                sign = 1
            elif num_list[i] == '-':
                sign = -1   # '-' 인 경우 음수로 설정

    # 마지막 숫자가 남아있을 경우, 결과에 추가
    if num:
        result += sign*int(num)

    print(result)

