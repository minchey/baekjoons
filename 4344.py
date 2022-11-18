T = int(input()) # 4344번 평균넘는 비율구하기
for _ in range(T):
    a = list(map(int, input().split()))
    b = sum(a[1:])/a[0]
    cnt = 0
    for i in a[1:]:
        if i > b:
            cnt +=1
    c = cnt/a[0]*100
    print(f'{c:.3f}%')
