import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())
arr = list(map(int, input().split()))

result = 0  # 변수를 생성할때는 위치/초기값 고민 후 작성
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if result<arr[i]+arr[j]+arr[k]<=M:
                result = arr[i]+arr[j]+arr[k]

print(result)


