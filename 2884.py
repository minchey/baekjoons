h , m = input().split() # 알람시계 2884
h = int(h)
m = int(m)
if h >=0 and m >= 45:
    print(h , m-45)
elif h >0 and m <45:
    print(h - 1, m +15)
else:
    print(23, m+15)
