# 백준 1260 DFS와 BFS

import sys
sys.stdin = open('input.txt')

N, M, V = map(int,input().split())
graph = [[False] * (N+1) for _ in range(N+1)]
# N+1 => 정점은 1~4까지, 0번째 인덱스 사용하지 않기 위해
print(graph)
# 연결된 정점을 입력
for i in range(M):
    x, y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited1 = [False] * (N+1)
visited2 = [False] * (N+1)






# DFS

