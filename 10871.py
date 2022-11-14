a , b = map(int, input().split())  # 10871번 x보다 작은수 찾아내기
a_list = list(map(int, input().split()))
for i in range(a):
    if b > a_list[i]:
        print(a_list[i])
