a = int(input()) #2441번 별 거꾸로 찍기오른쪽정렬
for i in range(a,0,-1):
    b = '*'
    c = b * i
    print(str(c).rjust(a))
