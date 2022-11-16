sums = 0 #10039번 평균구하기
for i in range(0,5):
    a =int(input())
    if a < 40:
        sums +=40 -a
    sums += a
print(int(sums/5))
