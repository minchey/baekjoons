while True : #11718번 그대로 출력 입력 받는대로
    try :
        print(input())
    except EOFError:
        break
