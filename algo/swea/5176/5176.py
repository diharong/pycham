import sys
sys.stdin = open('input.txt')

'''
왼 - 현 - 오 : 중위탐색

'''
def inorder(node):
    left = node * 2
    right = node * 2 + 1
    if left <= N:
        inorder(left)
    tree_inorder.append(node)
    if right <= N:
        inorder(right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    tree = list(range(N+1))
    tree_inorder = [0]
    inorder(node=1)
    print(tree_inorder)

    result = [0, 0]
    for i in range(len(tree_inorder)):
        if tree_inorder[i] == 1:
            result[0] = i
        if tree_inorder[i] == N//2:
            result[1] = i


    print(f'#{tc}', *result)