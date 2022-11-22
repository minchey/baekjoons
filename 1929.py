a , b = map(int, input().split()) # 1929번 소수구하기
for i in range(a, b+1):
    if i==1:#1은 소수가 아니므로 제외
        continue
    for j in range(2,int(i**0.5)+1): 
        if i%j ==0: #딱 떨어지면 약수가 존재함
            break
    else:
        print(i)
