import sys
sys.stdin = open('input.txt')


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())    # 단어의 길이
#     arr = list(str(input()))
#     # print(arr)
#
#     # 가장 긴 데칼코마니 길이를 저장할 변수를 초기화
#     max_value = 1
#
#     for center in range(N):
#         left = center - 1
#         right = center + 1
#         current_len = 1     # 중심만 포함하는 초기 길이는 1
#
#         # 좌우 대칭으로 비교 가능한 한 계속 비교할거임
#         # 만약 같은 숫자라면 바깥쪽도 계속 비교해.
#         while left >= 0 and right < N:
#             # 만약 왼쪽과 오른쪽이 다르다면, 더 이상 데칼코마니가 아니니 멈춰.
#             if arr[left] != arr[right]:
#                 break
#             # 왼쪽과 오른쪽이 같으면 데칼코마니 길이를 2만큼 늘려준다
#             current_len += 2
#             # 그리고 비교할 범위를 한 칸 더 바깥쪽으로 넓혀준다.
#             left -= 1   # -= 임 조심할것
#             right += 1
#
#         # 지금까지 찾은 데칼코마니 길이가 가장 길다면, 그 값을 업데이트
#         if max_value < current_len:
#             max_value = current_len
#
#
#     print(f'#{tc} {max_value}')



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(str(input())) # 10101
    # print(arr)


    max_value = 1       # 가장 긴 데칼코마니 길이 변수를 초기화

    for center in range(N):
         left = center - 1      # 왼쪽 값 변수 설정
         right = center + 1     # 오른쪽 값 변수 설정
         current_len = 1        # 현재 길이 1 변수 초기화

         # 데칼코마니가 안나올 때까지 돌려, 근데 왼,오 인덱스 조정해줘야대

         while 0 <= left and right < N and arr[left] == arr[right]:
             current_len += 2
             left -= 1
             right += 1


         if max_value < current_len:
             max_value = current_len

    print(max_value)



















