arr = [4, 5, 6, 1, 2, 3, 1, 2, 5, 6]
N = len(arr)


length = 1     # 증가값 찾았을때 길이추가
len_lst = []

for i in range(1, N):
    if arr[i-1] < arr[i]:
        length += 1
        len_lst.append(length)
    else:   # 증가 멈춤 확인
        length = 1  # 길이 다시 1로 초기화
print(max(len_lst))



