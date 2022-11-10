t = int(input()) #좀더 이쁘게 출력 11022
for i in range(1, t +1):
    a , b = map(int, input().split())
    c = a + b
    print(f'Case #{i}: {a} + {b} = {c}')
