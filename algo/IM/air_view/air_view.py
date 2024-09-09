# air view

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    view_1 = list(map(int,input().split())) # x1, y1, x2, y2
    view_2 = list(map(int,input().split()))  # x1, y1, x2, y2

    '''
    겹치는 영역 존재 - 1
    1번에 해당하지 않으며, 겹치는 선이 존재 - 2
    1,2 번에 해당하지 않으며, 겹치는 점이 존재 - 3
    1,2,3 번에 해당하지 않음. 안겹침 - 4
    
    출력 - 몇번 상태에 속하는지 출력
    '''

