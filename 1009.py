a = int(input()) # 1009번 분산처리 다시풀어보기
b = []
c = []
for i in range(a):
    num1 , num2 = input().split()
    b.append(int(num1))
    c.append(int(num2))
for j in range(a):
    base = b[j]%10
    if base == 0:
        print(10)
    elif base in [1,5,6]:
        print(base)
    elif base in [4,9]:
        if c[j] %2 ==0:
            print(base**2 % 10)
        else:
            print(base)
    else:
        if c[j]%4 ==0:
            print(base**4 %10)
        else:
            print(base**(c[j]%4)%10)
