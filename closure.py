x = 10


def foo():
    x = 20
    print(x)  # foo의 지역변수


def myfoo():
    global x
    x = 11
    print(x)


foo()
myfoo()
print(x)
print(locals())  # namespace
