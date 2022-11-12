a = int(input()) #2588번 세자리수곱셈
b = int(input())
c = a* (b%10)
d = a* (b//10%10)
f = a* (b//100)
print(c,d,f,a*b)
