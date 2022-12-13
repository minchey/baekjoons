def solution(n):
    answer = 0
    a = 6
    while True:
        b = a % n 
        if b ==0:
            answer = a // 6
            break
        a += 6
    return answer
