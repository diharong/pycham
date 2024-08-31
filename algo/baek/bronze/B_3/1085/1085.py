import sys
sys.stdin = open('input.txt')

x,y,w,h = map(int,input().split())

result = []
if h-y < y:
    result.append(h-y)
else:
    result.append(y)
if w-x < x:
    result.append(w-x)
else:
    result.append(x)

print(min(result))

'''
헐 ,,, 처음으로 혼자 풀어냄 
...........
눈물나......................
ㄹㅇ ,,,,,,,,,,,,
'''
