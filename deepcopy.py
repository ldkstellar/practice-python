import copy
myarray:list = [1,2,3,4,5]


a = [[10,20],[30,40]]
b=copy.deepcopy(a) # 이차원배열부터는 깊은 배열의 복사가 되지 않는다.
print(a)
print(b)