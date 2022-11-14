a_list = [] #3052번 리스트에서 같은값 제외하고 갯수찾기
for i in range(10):
    a = int(input())
    b = a % 42
    a_list.append(b)
    set(a_list)
print(len(set(a_list)))
