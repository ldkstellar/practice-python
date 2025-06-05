class Person:
    def greeting(self):
        print("안녕하세요")

class Student(Person):
    def greeting(self):
        super().greeting()
        print("안녕하세요 저는 파이썬 코딩도장 학생입니다.")# 오버라이딩
james = Student()
james.greeting()
# 파이썬에서 자식클래스에서 부모생성자를 호출하지 않으면 부모 멤버변수를 생성하지 않는다. 