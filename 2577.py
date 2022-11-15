a = int(input()) #2577번 숫자갯수세기
b = int(input())
c = int(input())
d = list(str(a* b* c)) # d 의값을 문자열로 받고 리스트화를 시켜준다
for i in range(0,10):
    print(d.count(str(i)))
