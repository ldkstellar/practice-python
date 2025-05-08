# 메
class Person:
    def __init__(self, name, age, adrres, id):
        self.hello = "안녕하세요"
        self.name = name
        self.age = age
        self.address = adrres
        self.__id = id

    def greeting(self):  # 첫번째함수는 self를 써줘야 한다.
        print("hello")


james = Person("이동규", 28, "hidden", 0)

james.greeting()
