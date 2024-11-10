import sys
sys.stdin = open('input.txt')

#   가장 높은 점수를 획득한 사람(번호) 와 점수 함께 출력

N, M = map(int,input().split())     # N 문제 , M 명의 학생
question = list(map(int,input().split()))
# for _ in range(M):
#     arr = list(map(str,input().split()))
arr = [list(map(str,input().split())) for _ in range(M)]

print(arr)
score = []

for i in range(M):
    for j in range(1, N+1):
        if arr[i][j] == 'O':
            score.append([arr[i][0], question[j-1]])

# print(score)

for item in score:
    pass



