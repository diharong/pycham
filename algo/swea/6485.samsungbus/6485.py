T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 노선수

    counts = [0] * 5001 # 5000번 정류장까지
    # N개의 노선 정보를 모두 읽어놓고 처리 or 읽을 때마다 처리 - 를 결정해야댐
    for _ in range(N):
        A, B = map(int, input().split()) # Ai -> Bi 버스 노선의 시점Ai와 종점Bi, Ai<=Bi
        for i in range(A, B+1):
            counts[i] += 1

    P = int(input())    # 노선수를 출력할 P개의 버스 정류장
    # 모두 읽어놓고 처리
    busstop = [int(input() for _ in range(P))]
    print(f'#{tc}', end = ' ')
    for j in busstop:
        print(counts[j], end=' ')
    print()

'''
테케가 하나만 주어졌을 경우 복붙해서 두개의 테케로 만들어 프린트 해본다
'''
