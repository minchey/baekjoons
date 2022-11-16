a , b = map(int, input().split()) #2908번 숫자거꾸로읽기
c = (a//100) + (((a%100)//10)*10) + ((a%10)*100)
d = (b//100) + (((b%100)//10)*10) + ((b%10)*100)
if c > d:
    print(c)
else:
    print(d)
