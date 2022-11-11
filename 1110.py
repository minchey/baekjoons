a = int(input())  #1110번 사이클 갯수찾기 ***
d = []
g = []
b = a//10 + a %10
c = b % 10 + a%10*10
d.append(c)
g.append(b)
if a <10:
    a*10
while True:
    e = d[-1]//10 + d[-1]%10
    f = e % 10 + d[-1]%10*10
    d.append(f)
    g.append(e)
    if d[-1] == a:
        break
if a==0:
    print(1)
else:
    print(len(g))
