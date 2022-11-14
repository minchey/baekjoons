a = int(input()) #1546번 시험점수 조작
b = list(map(int, input().split()))
sums = 0
for i in b:
    d = i/max(b)*100
    sums += d
f = sums/a
print('{:.5f}'.format(f))
