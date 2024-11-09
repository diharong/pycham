arr = [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1]
N = len(arr)
K = 3

cnt = 0
result = 0

for i in range(N):
    if arr[i] == 1:
        cnt += 1
    else:
        if K == cnt:
            result += 1
        cnt = 0

if K == cnt:
    result += 1

print(result)


