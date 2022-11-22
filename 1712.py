a , b , c = map(int, input().split()) # 1712번 손익분기점
if b >= c :
    print(-1)
else:
    print(a//(c - b)+1)
