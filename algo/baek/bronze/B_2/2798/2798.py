import sys
sys.stdin = open('input.txt')


N, M = map(int,input().split())
arr = list(map(int,input().split()))

sorted(arr)
result = []
for i in range(N):      #범위 N+1 했다가 아웃오브레인지 남
    for j in range(i+1, N):
        for z in range(j+1, N):
            S = arr[i] + arr[j] + arr[z]

            if S <= M:
                result.append(S)
            else:
                break

print(max(result))