a = input() #10809번 알파벳 위치 찾기
a = list(a)
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in b:
    
    if i in a:
        print(a.index(i))
    else:
        print(-1)
