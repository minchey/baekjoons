a = int(input()) #8958번 ox퀴즈 점수 내기 
for i in range(a):
    b = input()
    score = 0
    cnt = 0
    for j in range(len(b)):
        if b[j] == 'O':
            cnt += 1
            score += cnt
        elif b[j] == 'X':
            cnt =0
    print(score)
