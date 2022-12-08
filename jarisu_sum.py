def solution(n):
    answer = 0
    a = []
    for i in range(len(str(n))-1,0,-1):
        b = n//10**i
        a.append(b)
        n -= b*(10**i)
    for j in range(len(a)):
        answer += a[j]
    answer += n%10
    return answer
