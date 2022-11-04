a , b ,c = input().split() #주사위상금 2480
a = int(a)
b = int(b)
c = int(c)
if a == b == c:
    print(10000 + a * 1000)
elif a == b:
    print(1000 + 100*a)
elif a == c:
    print(1000 + 100*a)
elif c == b:
    print(1000 + 100*b)
elif a!= b!= c:
    print(100*max(a,b,c))
