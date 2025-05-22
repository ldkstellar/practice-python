fruits={"grape","orange","pineapple","cherry"} # 세트는 요소의 순서가 정해지지 않음 출력시 순서가 다르게 나온다.
print(fruits)

a = "grape" in fruits
print(a)
b = "baek" not in fruits
print(b)
c =  set("apple")
print(c)
d = set(range(5))
print(d)
# 빈세트 만들기
e = set()
#frozenset
f = frozenset(range(10))
print(f)