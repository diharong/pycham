import sys
sys.stdin = open('input.txt')

arr = list(input().strip())

print(arr)
word = ''
result = 0
for i in range(len(arr)):
    idx = i+1
    if arr[i] == '[':
        while arr[idx] != ']':
            word += arr[idx]
            idx += 1
        else:
            result += int(word)
        word = ''

    elif arr[i] == '{':
        while arr[idx] != '}':
            word += arr[idx]
            idx += 1
        else:
            result *= int(word)
        word = ''

print(result)






# lst = list(input())
# word = ''
# result = 0
# for i in range(len(lst)):
#     idx = i + 1
#     if lst[i] == '[':
#         while lst[idx] != ']':
#             word += lst[idx]
#             idx += 1
#         else:
#             result += int(word)
#         word = ''
#
#     if lst[i] == '{':
#         while lst[idx] != '}':
#             word += lst[idx]
#             idx += 1
#         else:
#             result *= int(word)
#         word = ''
#
# print(result)