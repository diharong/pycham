# 2c_솔빙 괄호계산기 - 그리디 너너어어어어무어려   ㅂ닫다아ㅏ앙아ㅏㅏ아아앙아

import sys
sys.stdin = open('input.txt')

string = list(str(input()))

print(string)


result = 0

for i in range(len(string)):
    word = ''
    if string[i] == '[':
        j = i+1
        while string[j] != ']':
            word += string[j]
            j = j+1
        result += int(word)

        # print(word)
        # print(result)

# for i in range(len(string)):
    if string[i] == '{':
        j = i+1
        while string[j] != '}':
            word += string[j]
            j = j+1
        result *= int(word)

        # print(word)
print(result)


