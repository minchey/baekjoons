a = int(input()) # 10807 개수세기
a_list = list(map(int, input().split()))  # map 함수는 list 나 tuple로 변형 시켜줘야한다
b = int(input())
print(a_list.count(b))
