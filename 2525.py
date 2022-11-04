a , b = input().split()  #오븐 2525
c = input()
a = int(a)
b = int(b)
c = int(c)
d = b + c
n = d//60
j = d%60
i = a + n
if i ==24:
    print(0 , j)
elif i >24:
    print(i -24 , j)
else:
    print(i , j)
