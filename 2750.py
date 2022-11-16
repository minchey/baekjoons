a = int(input()) #2750번 리스트만들고 오름차순으로 출력
b = []
for i in range(a):
    c = int(input())
    b.append(c)
    b.sort()
for j in range(len(b)):
    print(b[j])
