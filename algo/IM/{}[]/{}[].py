# 2반 솔빙 괄호계산기 - 그리디

import sys
sys.stdin = open('input.txt')

string = list(str(input()))

# print(string)

result = 0          # 연산결과

for i in range(len(string)):
    if string[i] == '[':
        while string[i] != ']':
            result += int(string[i])
            i = i+1

print(result)

