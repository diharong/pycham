import sys
sys.stdin = open('input.txt')

# 가장 높은 점수 - 가장 낮은 점수

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split()) # N 학생 수 , M 문제 수
    ans_lst = list(map(int,input().split()))
    student_lst = [list(map(int,input().split())) for _ in range(N)]
    # print(student_lst)

    score = 0   # 점수를 담을 변수

    result = []     # 점수 합들을 담을 리스트

    for i in range(N):

        personal_score = []
        # 각 학생들의 점수를 담을 빈 리스트

        for j in range(M):
            if ans_lst[j] == student_lst[i][j]:    # 만약에 정답이면,
                score += 1
                personal_score.append(score)
            else:   # ans_lst[j] != student_lst[i][j]:
                # if score > 0:
                #     personal_score.append(score)
                score = 0

        if score > 0:
            score = 0

        result.append(sum(personal_score))

    result = max(result) - min(result)

    print(f'#{tc}', result)



