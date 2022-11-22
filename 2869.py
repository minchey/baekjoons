a , b , v = map(int, input().split()) #2869번 달팽이는 올라가고싶다
c = 0
if (v - b )% (a - b)>0:
    c = (v - b) // (a -b)+1
else:
    c = (v -b) //(a - b)
print(c)
