t = int(input()) #11021번 이쁘게 출력하기
for i in range(1, t +1):
    a , b = map(int, input().split())
    c = a + b
    print(f'Case #{i}: {c}')
