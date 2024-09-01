# 1231. [S/W 문제해결 기본] 9일차 - 중위순회

import sys
sys.stdin = open('input.txt')

def search(node):
    global res
    if node == 0 :
        return
    search(tree[node][0])
    res += result[node]
    search(tree[node][1])


for tc in range(1, 11):
    N = int(input())    # 트리 정점 수
    arrs = [list(str(input()).split()) for _ in range(N)]
    print(arrs)
    tree = [[0, 0] for _ in range(N+1)] # 0번 인덱스 안쓰기 위해
    # print(tree)
    result =[0]     # 단어를 담을 리스트

    # 각 arr 들을 원소 4개씩 맞춰줘야함
    for arr in arrs:
        while len(arr) != 4:       # 꼭 while 문을 돌려야 하는가에 대해.
            arr.append('0')
        result.append(arr[1])
        tree[int(arr[0])][0] = int(arr[2])
        tree[int(arr[0])][1] = int(arr[3])

    res = ' '

    print(result)
    print(tree)







