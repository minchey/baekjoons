import math
def solution(price):
    answer = 0
    if 300000 > price >= 100000:
        answer = math.trunc(price * 0.95)
    elif 500000 > price >= 300000:
        answer = math.trunc(price * 0.9)
    elif price >= 500000:
        answer = math.trunc(price * 0.8)
    elif price < 100000:
        answer = price
    return answer
