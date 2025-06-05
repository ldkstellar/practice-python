class Knight:
    __item_limit = 10    # 비공개 클래스 속성
 
    def print_item_limit(self):
        print(Knight.__item_limit)    # 클래스 안에서만 접근할 수 있음
class Person:
    bag = []
    def put_bag(self,stuff):
        Person.bag.append(stuff)
class Myperson:
    def __init__(self):
        self.bag = []
    def put_bag(self,stuff):
        self.bag.append(stuff)

x = Knight()
x.print_item_limit()    # 10
# 클래스 바깥에서는 접근할 수 없음

james = Person()
james.put_bag("책")
maria = Person()
maria.put_bag("열쇠")

print(james.bag)
print(maria.bag)
# 클래스 속성은 클래스에 속해 있으며 모든 인스턴스에서 공유한다.

john = Myperson()
john.put_bag("책")
mary =  Myperson()
mary.put_bag("열쇠") 
print(john.bag)
print(mary.bag)