a_list = [] #2562번 최댓값과 순서 출력 (세로로입력)
for i in range(9):
    a = int(input())
    a_list.append(a)
for i , j in enumerate(a_list):
    if j == max(a_list):
        print(j)
        print(i+1)
