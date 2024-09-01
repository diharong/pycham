import sys
sys.stdin = open('input.txt')


# def text(length, table):
#     cnt = 0
#     for i in range(8):
#         for j in range(8):
#             if j + length > 8:  # 만약에 범위를 넘어가면 break 해줘야한다는거 중요해
#                 break
#
#             R_Text = table[i][j:j + length]  # 가로버전
#             if R_Text == R_Text[::-1]:  # 오른쪽 방향이랑 왼쪽방향으로 읽은게 같은 경우 cnt에 1씩 추가
#                 cnt += 1
#
#             C_Text = []
#             for k in range(length):  # 세로버전
#                 C_Text.append(table[j + k][i])
#             if C_Text == C_Text[::-1]:
#                 cnt += 1
#     return cnt
#
#
# T = 10
# for t in range(1, T + 1):
#     length = int(input())
#     table = [list(input()) for _ in range(8)]
#     cnt = text(length, table)
#     print(f"#{t} {cnt}")


# def text(length, table):
#     cnt = 0
#     for i in range(8):
#         for j in range(8):
#             if j + length > 8:
#                 break
#
#             R_Text = table[i][j:j+length]
#             if R_Text == R_Text[::-1]:
#                 cnt += 1
#
#             C_Text = []
#             for k in range(length):
#                 C_Text.append(table[j+k][i])
# #             if C_Text == C_Text[::-1]:
# #                 cnt += 1
# #
# #     return cnt
# #
# #
# # T = 10
# # for tc in range(1, T+1):
# #     length = int(input())
# #     table = [list(input()) for _ in range(8)]
# #     cnt = text(length, table)
# #     print(f'#{tc} {cnt}')
#


# T = 10
# for tc in range(1, T+1):
#     length = int(input())
#     arr = [list(input()) for _ in range(8)]
#
#     cnt = 0         # 회문의 개수 카운팅할 변수 초기화
#
#     # 가로 버전
#     for i in range(N):
#         for j in range()


# T = 10
# for tc in range(1, T+1):
#
#     # palindrome 의 길이 입력
#     p = int(input())
#     # 평면 글자판은 8x8
#     N = 8
#     # 글자판 입력
#     arr = [list(input()) for _ in range(N)]
#
#     # 회문의 수를 구하기 위해 변수 초기화
#     cnt = 0
#
#     # 가로일 때
#     for i in range(0, N):
#         for j in range(0, N-p+1):
#             # 글자판 i번째 행의 j번째 열부터 회문의 길이만큼의 문장과 그 역순 문장이 같으면
#             if arr[i][j:j+p] == arr[i][j:j+p][::-1]:
#                 # 회문이므로, cnt에 1을 더해준다.
#                 cnt += 1
#
#     # 세로일 때
#     for j in range(0, N):
#         for i in range(0, N-p+1):
#             # 세로 문장을 확인하기 위해 char 변수 생성 및 초기화
#             char = ''
#             # i번째 행부터 회문의 길이만큼 문자열을 char 변수에 저장
#             for ci in range(i, i+p):
#                 char += arr[ci][j]
#             # char 문장과 그 역순 문장이 같으면 회문이므로, cnt에 1을 더해준다.
#             if char == char[::-1]:
#                 cnt += 1
#
#     # 결과 출력
#     print('#{} {}'.format(tc, cnt))


T = 10
for tc in range(1, T+1):
    P = int(input())
    N = 8
    arr = [list(input()) for _ in range(N)]

    cnt = 0

    # 가로일때
    for i in range(0, N):
        for j in range(0, N-P+1):
            if arr[i][j:j+P] == arr[i][j:j+P][::-1]:
                cnt += 1

    # 세로일때
    for j in range(0, N):
        for i in range(0, N-P+1):
            char = ''
            for ci in range(i, i+P):
                char += arr[ci][j]
            if char == char[::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')



