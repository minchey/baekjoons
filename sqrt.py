import math
def solution(n):
    sqrt = math.sqrt(n)
    if sqrt == int(sqrt):
        answer = 1
    else:
        answer = 2
    return answer
