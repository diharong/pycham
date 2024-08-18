import sys
sys.stdin = open('input.txt')
#
# N = int(input())
#
# # for i in range(1, N+1):         # 1부터 N 까지 숫자니까
# #     cnt = str(i).count('3') + str(i).count('6')+str(i).count('9')
# #     if not cnt:
# #         print(i, end=' ')
# #     else:
# #         print('-'*cnt, end=' ')
#
# for i in range(1, N+1):     # 1부터 N까지 반복
#     s = str(i)              # i번째 숫자를 문자로 변환
#     cnt = 0               # i 번째 숫자가 3, 6, 9를 몇개 포함하고 있는지 카운팅하기 위한 변수
#
#     for j in s :            # 문자로 변환한 i번째 숫자를 한 자리씩 반복한다. 369 => [3, 6, 9]
#         if (j == '3') or (j == '6') or (j == '9'):  # 3, 6, 9 문자가 있으면
#             cnt += 1                    # 1씩 카운팅해준다.
#
#     if cnt == 0:                # cnt 이 0 이면 (3, 6, 9 가 미포함이므로)
#         print(i, end=' ')       # i를 그대로 출력
#
#     else:                       # cnt 가 존재하면
#         print(cnt*'-', end=' ') # cnt 수 만큼 - 를 출력 36일경우 cnt 가 2 이므로 -- 출력
#



N = int(input())





