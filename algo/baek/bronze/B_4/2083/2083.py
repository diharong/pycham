# 백준 럭비클럽

import sys
sys.stdin = open('input.txt')

# T = 4
# for tc in range(1, T+1):
arr = list(input().split())


if int(arr[1]) > 17 or int(arr[2]) >= 80:
    print(f'{arr[0]}', 'Senior')

else:
    print(f'{arr[0]}', "Junior")








