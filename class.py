# Class
class Class_name():  #클래스명은 대문자로 시작
  def __init__(self,name): # init은 생성자함수, self 는 클래스를 저장할 변수
    self.name = name
    print(self.name)
a = Class_name('kmc')  #클래스 실행 생성자가 실행이 되고 name = kmc가 입력됨
a.name() # print(self.name)이 실행 kmc가 출력된다
