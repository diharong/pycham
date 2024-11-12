import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # # print(N)
    #
    # # 아직 본적이 없는 숫자 리스트
    # num_list = [i for i in range(0,10)]
    #
    # # 배수를 늘려가면서 확인하기 위해  K 변수 를 1로 초기화 0아님!
    # count = 1
    #
    # # for i in num_list:
    # #     while N not in num_list:
    # #         count += 1
    #
    # # 모든 숫자를 다 볼때까지 반복
    # while len(num_list) !=0:
    #     M = N*count
    #     for j in str(M):
    #         j = int(j)  # 각 자리숫자를 정수로 변환
    #         # 만약 아직 확인하지 않은 숫자라면 리스트에서 제거
    #         if j in num_list:
    #             num_list.remove(j)
    #
    #     count +=1
    #
    # print(M)

    # 0부터 9까지의 숫자를 모두 볼때까지 추적하기 위한 집합
    num_list = set()

    # 현재 배수 값을 저장할 변수
    current_num = 0

    while len(num_list) < 10:
        current_num += N

        for i in str(current_num):
            num_list.add(i)

    print(current_num)


