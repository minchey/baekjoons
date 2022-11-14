while True: #입력이 끝날때 까지 10951번
    try:
        A, B = map(int, input().split())
        print(A+B)
    except EOFError:
        break
# except를 이용하여 예외가 발생하였을때 문제처리를 할 수 있다
