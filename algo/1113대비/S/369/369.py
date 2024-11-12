import sys
sys.stdin = open('input.txt')

N = int(input())

game = [str(i) for i in range(1, N+1)]
clap = 0
for g in range(len(game)):
    if '3' in game[g] or '6' in game[g] or '9' in game[g]:
        clap = game[g].count('3') + game[g].count('6') + game[g].count('9')
        game[g] = '-'*clap
        clap = 0

print(*game)