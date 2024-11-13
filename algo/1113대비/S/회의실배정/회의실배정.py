import sys
sys.stdin = open('input.txt')

N = int(input())
time = [list(map(int,input().split())) for _ in range(N)]
# time = []
# for _ in range(N):
#     start,end = map(int,input().split())
#     time.append([start, end])
time.sort(key=lambda x:x[1])
cnt = 0
before_e = 0
for start,end in time:
    if start >= before_e:
        cnt+=1
        before_e = end
print(cnt)


# T = int(input())
# time = []
# for _ in range(T):
#     s,e = map(int,input().split())
#     time.append([s,e])
# time.sort(key=lambda x:x[1])
# cnt = 0
# end = 0
# for s,e in time:
#     if s >= end:
#         cnt += 1
#         end = e
# print(cnt)