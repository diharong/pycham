import sys
sys.stdin = open('input.txt')

N = int(input())        # 노드의 개수
tree = [[] for _ in range(N+1)]
visited = [False] * (N+1)
# print(visited)
result = [0] * (N+1)
# print(result)

def dfs(node):
    visited[node] = True
    for i in tree[node]:
        if visited[i] == False:
            result[i] = node
            dfs(i)




# N-1 개의 줄에 트리 상에 연결된 두 정점
for _ in range(1, N):
    num1, num2 = map(int,input().split())

    tree[num1].append(num2)
    tree[num2].append(num1)

dfs(1)
for i in range(2, N+1):
    print(result[i])


