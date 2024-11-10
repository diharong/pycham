import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int,input().split()))

# 오르막길의 크기 = 마지막 숫자 - 첫 번째 숫자

max_value = 0   # 최대값
dist = 0    # 각 길의 높이 차이

for i in range(1, N):
    # i가 1부터 시작하는 이유는 이전 인덱스값을 비교하기 위해 ,
    # 0번 인덱스는 비교를 위해 쓰이므로 1번부터 시작해야한다.
    if arr[i]-arr[i-1] > 0:     # 만약에, 현재인덱스와 이전인덱스의 차이가 0보다 클 경우 => 오르막으로 판단.
        dist += arr[i]-arr[i-1]     # 그 차이를 dist 변수에 담아준다.

    else:                       # 만약, 차이가 0보다 작거나 같을 경우 => 오르막 X
        max_value = max(max_value, dist)    # 이전까지 담아온 dist 변수값과 max_value 값을 비교하여 max_value 값을 갱신해준다.
        dist = 0            # 그리고 dist 값은 다시 0으로 초기화하여 다음 차이값을 담을 준비를 한다.
        i += 1              # 다음 값을 비교하기 위해 i를 1증가시킨다.

# for 문이 종료되었을 때 최종적으로 남아있는 dist 값과 max_value 값을 비교하여, 최종 답을 도출해낸다.
if max_value < dist:
    max_value = dist

print(max_value)











# 가장 긴 오르막의 길이 구하기

# cnt = 0     # 오르막 길이를 남을 변수
# current_check = 0
# max_value = 0
#
# for i in range(N):
#     if arr[i] > current_check:
#         cnt += 1
#         current_check = arr[i]
#
#     else:   # arr[i] <= current_check:
#         max_value = max(cnt, max_value)
#         cnt = 0
#         current_check = arr[i]
#         cnt += 1
# max_value = max(cnt, max_value)
#
# print(max_value)





