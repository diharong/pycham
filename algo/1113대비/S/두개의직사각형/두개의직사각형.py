import sys
sys.stdin = open('input.txt')



T = int(input())
for tc in range(1, T+1):
    box1 = list(map(int,input().split()))
    box2 = list(map(int,input().split()))

    x1 = box1[0]
    y1 = box1[1]
    x2 = box1[2]
    y2 = box1[3]

    x3 = box2[0]
    y3 = box2[1]
    x4 = box2[2]
    y4 = box2[3]

    # 영역이 겹칠 때
    if x3 < x2 and y3 < y2 and x1 < x4 and y1 < y4:
        print('1')
    # 선이 겹칠 때
    elif (x2 == x3 or x1 == x4) and  y2 > y3 :
        pass













# def check(rect1, rect2):
#     x1, y1, x2, y2 = rect1
#     x3, y3, x4, y4 = rect2
#
#     # 면이 겹칠때
#     if x3 < x2 and y3 < y2 and x1 < x4 and y1 < y4:
#         return 1
#     # 선이 겹칠때
#     elif (x2 == x3 or x4 == x1) and y3 < y2 and y1 < y4:
#         return 2
#     elif (y2 == y3 or y4 == y1) and x3 < x2 and x1 < x4:
#         return 2
#     # 점이 겹칠때
#     elif (x2 == x3 and y2 == y3) or (x2 == x3 and y1 == y4) or (x1 == x4 and y2 == y3) or (x1 == x4 and y1 == y4):
#         return 3
#     # 겹치는 부분이 아예 없을때
#     return 4
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     rect1 = map(int, input().split())
#     rect2 = map(int, input().split())
#     result = check(rect1, rect2)
#     print(f'#{tc} {result}')