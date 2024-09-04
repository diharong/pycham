import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(str(input()))

    stack = []

    for i in range(len(arr)):
        stack.append(arr[i])
        if stack[i] == stack[-1]:
            stack.pop()

    print(stack)
    #
        # while stack != 0:
        #
        #     print(stack)
        #     if stack[i] == stack[i+1]:
        #         stack.pop()
        #
        # print(stack)

    # li = []
    #
    # for i in range(len(arr)-1):
    #     if arr[i] == arr[i+1]:
    #         li.append(arr[i])




