def solution(array):
    answer_list = []
    for i in set(array):
        a = array.count(i)
        answer_list.append(a)
        if a == max(answer_list):
            answer = i
    if answer_list.count(max(answer_list)) > 1 :
        answer = -1
    return answer
