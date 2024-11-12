import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    sample = list(map(int,input().split()))
    passcode = list(map(int,input().split()))


    check_point = 0

    for num in passcode:
        if num in sample[check_point:]:


