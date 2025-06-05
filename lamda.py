def plus_ten(x):
    return x + 10

# 일반적인 함수

lambda_def = lambda x: x + 10  # 람다 표현식안에 새로운 변수를 만들 수없다.

# and or not 을 사용한다.

array = list(())
array.append(plus_ten(1))
array.append(lambda_def(1))
print(array)

test = list(map(lambda x: x + 10, [1, 2, 3]))
print(test)
sample = (lambda x: x + 10)(1)
print(sample)
