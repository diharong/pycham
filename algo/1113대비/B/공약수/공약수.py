'''
공약수

두 수 A와 B가 주어졌을 때,
두 수의 GCD(최대공약수) 와 LCM(최소공배수)를 계산해서구하시오.
'''

'''
1. 갭을 줄여도 된다!

# 8 12
# 4 8

2. 최대 공약수라는 말은 두 수 중 하나로 나누어서 나머지가 생기지 않는 것을 말함
8 12 -> 8로 12를 나누면 나머지가 생긴다. 나머지는 4

4 8 -> 하지만 4로 8을 나누면 나머지가 생기지 않는다.
이때 , 두 수를 서로 나누려고 할 때 나머지가 생기지 않으면
이 두 수중 작은 수가 최대공약수가 된다. =>4

3. 한 수를 가능한 만큼 갭을 줄인다.
하나의 수를 작은수로 되는 만큼 뺀다는 말은
나누고 나서 나머지를 뜻한다.

121 7
121-7-7-7-7-7-7...
121%7 와 같다.

'''
# 최대공약수
def _gcd(a,b):
    while a % b != 0: # 나머지가 0이 되는 순간 멈춘다. => 최대공약수를 찾으면 멈춘다.
        tmp = a%b
        a = b
        b = tmp
    return b
# ????

# 최소공배수
def _lcm(a,b):
    return a*b//_gcd(a,b)