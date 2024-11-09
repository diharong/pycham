# 연속한 1의 최대 개수 구하기

arr = [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]
N = len(arr)

cnt = 0 # 1 카운트
result = 0  # 연속한1의 최대 개수
for i in range(N):
    if arr[i] == 1:
        cnt += 1
        if result < cnt:
            result = cnt
    else:
        cnt = 0
print(result)
