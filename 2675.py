T = int(input()) #2675번 문자열 반복
a_list = []
q = ''
for i in range(T):
    r , s = input().split()
    r = int(r)
    
    for j in range(len(s)):
       print(s[j]*r, end='')
    print()
