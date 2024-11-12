import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    answer = list(map(int,input().split()))
    student = [list(map(int,input().split())) for _ in range(N)]

    # 가장 높은 점수 학생 - 가장 낮은 점수 학생

     # 정답이면 카운트할 변수

    class_S = []    # 학생들의 점수 총합을 모을 빈 리스트

    for i in range(N):
        cnt = 0
        personal_S = 0  # 점수 총합
        for j in range(M):
            if answer[j] == student[i][j]:
                cnt += 1
                personal_S += cnt
                personal_S = max(cnt,personal_S)
            else:   # 정답이 틀렸을 경우
                # if cnt > 0: # 근데 이전 카운트가 남아있는경우
                #     personal_S += cnt
                #     personal_S = max(cnt, personal_S)
                #     class_S.append(personal_S)
                cnt = 0 # 정답카운트를 초기화 즉, 합계에 넣지 않는다.
        if cnt > 0:
            # personal_S += cnt
            personal_S = max(cnt, personal_S)
        class_S.append(personal_S)

    print(f'#{tc}' , max(class_S)-min(class_S))
