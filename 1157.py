a = input() #1157번 단어공부
a = a.upper() #대문자로 바꿔준다
b = list(set(a)) # 중복 단어를 없애준다
b_list = []
for i in b:
    cnt = a.count(i) #주어진단어에 i가 얼마나 있는지 센다
    b_list.append(cnt) #리스트에 추가
if b_list.count(max(b_list)) >1: #최댓값이 1개 보다 많은지 판별
    print('?')
else:
    index = b_list.index(max(b_list)) #인덱스값을 얻어내 원하는 알파벳 찾기
    print(str(b[index]))
