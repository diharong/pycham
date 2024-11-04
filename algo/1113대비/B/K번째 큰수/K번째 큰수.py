import sys
sys.stdin = open('input.txt')
'''
현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있다. 같은 숫자의 
카드가 여러장 있을 수 있다. 현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 
합한 값을 기록하려 한다. 기록한 값 중 K번째로 큰 수를 출력하는 
프로그램을 작성하라
만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19 ... 이고 
K값이 3이라면 k번째 큰 값은 22이다.
'''


N, K = map(int,input().split()) # 자연수 N K
arr = list(map(int,input().split()))

res=set() #중복제거

for i in range(N):
    for j in range(i+1, N):
        for z in range(j+1, N):
            res.add(arr[i]+arr[j]+arr[z])

res=list(res)
res.sort(reverse=True) #내림차순
print(res[K-1]) #143