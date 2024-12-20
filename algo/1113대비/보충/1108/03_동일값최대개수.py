arr = [0, 0, 2, 2, 1, 3, 2, 2, 2, 1, 1, 1, 1]
N = len(arr)

cnt = 0 #

for i in range(1, N):
    if arr[i] == arr[i-1]:
        cnt += 1
    else:       # 만약, 자신의 이전 인덱스와 값이 다르면
        cnt = 0     # 카운팅 값 초기화


# arr = [0, 0, 2, 2, 1, 3, 2, 2, 2, 1, 1, 1, 1]  # 입력 배열
# N = len(arr)  # 배열의 길이
#
# ans = 0  # 최대 연속 개수를 저장할 변수
# cnt = 1  # 연속된 동일 값의 개수를 세기 위한 초기값 (1부터 시작)
#
# for i in range(1, N):  # 배열의 첫 번째 값은 비교에 사용되었으므로 1부터 시작
#     if arr[i - 1] == arr[i]:  # 이전 값과 현재 값이 같다면
#         cnt += 1  # 동일 값 개수 1 증가
#         if ans < cnt:  # 현재 최대 연속 개수보다 크면 갱신
#             ans = cnt
#     else:  # 값이 달라진 경우
#         cnt = 1  # cnt 를 1로 초기화하여 새로운 연속 개수 세기 시작
#
# # 마지막 연속 개수를 최종적으로 최대값과 비교
# # if ans < cnt: ans = cnt  # 필요 시 주석 해제하여 사용 가능
# print(ans)  # 최대 연속 동일 값 개수 출력

