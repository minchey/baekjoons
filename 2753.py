a = input() #윤년구하기 	2753
a = int(a)
if a%100 ==0 and a%400!=0:
    print(0)
elif a% 4 ==0 and a%100!=0:
    print(1)
elif a% 400==0 and a%100==0:
    print(1)
elif a% 400!=0 :
    print(0)
else:
    print(0)
