import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # ' + ' 방향 배열 탐색
    dx = [0, 1, 0, -1]  # 상우하좌
    dy = [1, 0, -1, 0]

    max_value1 = 0   # ' + ' 방향 탐색에서 최대 파리 수 저장할 변수 초기화

    for x in range(N):  # 행을 순회
        for y in range(N):  # 열을 순회

            current_point = arr[x][y]   # 현재 위치의 파리 수 초기화

            # + 모양으로 M 거리까지 탐색하는 코드
            for k in range(4):  # 4방향 탐색
                for z in range(1, M):   # 1부터 M 전까지 탐색
                    nx = x + dx[k]*z  # 다음 행의 좌표 (이동방향 지정)
                    ny = y + dy[k]*z    # 다음 열의 좌표 (이동방향 지정)

                    # 배열 범위 안에 있는지 확인
                    if 0 <= nx < N and 0 <= ny < N:     # 다음 이동할 좌표가 NXN 배열 범위 안에 있다면
                        current_point += arr[nx][ny]    # 이동한 위치의 파리 수를 추가한다.

            # 최대 파리 수 업데이트
            if max_value1 < current_point:
                max_value1 = current_point

    # ' X ' 방향 배열 탐색
    di = [1, 1, -1, -1]
    dj = [-1, 1, 1, -1]

    max_value2 = 0  # ' X ' 방향 탐색에서 최대 파리 수 저장할 변수 초기화

    for i in range(N):  # 행을 순회
        for j in range(N):  # 열을 순회

            current_point_1 = arr[i][j]     # 현재 위치의 파리 수 초기화

            # X 모양으로 M 거리까지 탐색하는 코드
            for g in range(4):  # 4방향 탐색
                for h in range(1, M):   # 1부터 M 전까지 탐색
                    ni = i + di[g] * h      # 다음 행의 좌표 (이동방향 지정)
                    nj = j + dj[g] * h      # 다음 열의 좌표 (이동방향 지정)

                    #  배열 범위 안에 있는지 확인하는 코드
                    if 0 <= ni < N and 0 <= nj < N: # 다음 이동할 좌표가 NXN 배열 범위 안에 있다면
                        current_point_1 += arr[ni][nj]  # 이동한 위치의 파리 수를 추가한다.

            # 최대 파리 수 업데이트
            if max_value2 < current_point_1:
                max_value2 = current_point_1

    # 결과값 도출 = ' + ' 방향 탐색과 ' x ' 방향 탐색을 통해 나온 파리 수 중 최대값을 결과값 변수에 넣는다.
    result = max(max_value1, max_value2)

    print(f'#{tc}', result)



