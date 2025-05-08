# 메
class Person:
    def __init__(self, name:str, age:int, adrres:str, id:int):
        self.hello = "안녕하세요"
        self.name = name
        self.age = age
        self.address = adrres
        self.__id = id

    def greeting(self):  # 첫번째함수는 self를 써줘야 한다.그리고 멤버 변수에 접근하기 위해서는 self를 써야 한다.
        print("hello")
    def getId(self):
        print(self.__id)


james = Person("이동규", 28, "hidden", 0)

james.greeting()
