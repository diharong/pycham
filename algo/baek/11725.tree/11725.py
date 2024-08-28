import sys
sys.stdin = open('input.txt')

N = int(input())

visited = [False] * (N+1)
result = [0] * (N+1)

# print(visited)
# def search(node):   # node 우리가 방문한 노드(인덱스)
#     visited[node] = True
#     for i in tree[node]:    # for i in len(tree[node]) => tree[node][i]
#         if visited[i] == False :    # 방문안했따면
#             result[i] = node        # 부모를 result 에 담는다
#             search(i)               # 자식이자식아;/


def dfs(node):
    st = []
    st.append(node)
    while st:
        temp = st.pop()
        visited[temp] = True
        for i in tree[temp]:
            if visited[i] == False:
                st.append(i)
                result[i] = temp



tree = [[] for _ in range(N+1)]

for _ in range(1, N):
    num1, num2 = map(int, input().split())

    tree[num1].append(num2)
    tree[num2].append(num1)

# search(1)
dfs(1)
for i in range(2, N+1):
    print(result[i])






