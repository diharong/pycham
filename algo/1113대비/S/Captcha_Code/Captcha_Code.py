import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    sample = list(map(int,input().split()))
    passcode = list(map(int,input().split()))
    print(passcode)
    exist = []
    # 생성할 수 있으면 1, 아니면 0 출력
    passcode_copy = passcode.copy()
    for i in range(N):
        if sample[i] in passcode_copy:
            exist.append(sample[i])
            passcode_copy.remove(sample[i])

    if exist == passcode:
        result = 1
    else:
        result = 0

    print(f'#{tc}', result)

    # 테케 1개가 안맞음 ,, ;;

    


