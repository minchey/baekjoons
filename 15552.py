import sys  #input 보다 빠른 입력을 받기위해 쓰는 명령어 sys.stdin.readline().split()
T = int(input()) #Test case
for i in range(T):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)
