# 메
class Person:
    def __init__(self, name:str, age:int, adrres:str, id:int):
        self.hello = "안녕하세요"
        self.name = name
        self.age = age
        self.address = adrres
        self.__id = id #private 멤버 변수

    def greeting(self):  # 첫번째함수는 self를 써줘야 한다.그리고 멤버 변수에 접근하기 위해서는 self를 써야 한다.
        print("hello")
    def getId(self):
        print(self.__id) # 

class Student(Person): # 부모 생성자로 호출 파생클래스 생성자 안해도 부모클래스생성자 자동호출됨
    def __init__(self, name, age, adrres, id):
        super(Student,self).__init__(name, age, adrres, id)
    def study(self):
        print("공부하기")

james = Person("이동규", 28, "hidden", 0)
james.greeting()

lee = Student("lee",13,"suwon",1)
lee.study()