import sys
sys.stdin = open('input.txt')

N = int(input())
names = [input().strip() for _ in range(N)]

# print(name_lst)

def is_good_name(name):
    # 조건 1: 소문자만 사용할 것
    if not name.islower():
        return False

    # 조건 2: 특수문자 사용 금지 (영문 소문자만 있는지 확인)
    if not name.isalpha():
        return False

    # 조건 3: 같은 알파벳이 2개 이하로만 사용될 것
    for char in set(name):
        if name.count(char) > 2:
            return False

    # 조건 4: 모음 (a, e, i, o, u) 알파벳을 3개 이상 사용할 것
    vowels = 'aeiou'
    vowel_count = sum(1 for char in name if char in vowels)
    if vowel_count < 3:
        return False

    return True

#
# # 입력 처리
# n = int(input().strip())
# names = [input().strip() for _ in range(n)]

# 출력
for name in names:
    if is_good_name(name):
        print("good")
    else:
        print("no")
