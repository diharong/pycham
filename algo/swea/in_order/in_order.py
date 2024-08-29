import sys
sys.stdin = open('input.txt')

def search(node):
    global res
    if node == 0:
        return
    search(tree[node][0])
    res += result[node]
    search(tree[node][1])

for tc in range(1, 11):

    N = int(input())
    arrs = [list(input().split()) for _ in range(N)]
    tree = [[0, 0] for _ in range(N + 1)]
    result = [0]

    for arr in arrs:
        while len(arr) != 4:
            arr.append(0)
        result.append(arr[1])
        tree[int(arr[0])][0] = int(arr[2])
        tree[int(arr[0])][1] = int(arr[3])
    res = ''
    # print(tree)
    # print(result)
    search(1)
    print(f'#{tc} {res}')









    # for i in range(N+1):
    #     left = arr[2]
    #     right = arr[3]
    #     if left != 0:
    #         tree[arr[i]].append(left)
    #     if right != 0:
    #         tree[arr[i]].append(right)


