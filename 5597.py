a_list = []  #5597번 과제제출 안한번호
for i in range(28):
    a = int(input())
    a_list.append(a)
f = []
for j in range(1,31):
    if  j not in a_list:
        f.append(j)
print(min(f))
print(max(f))
