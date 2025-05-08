str = "my name is leedongkyu"

for i in range(str.__len__()):
    if (i == str.__len__()-1):
         print(str[i], end="\n")
    else:
           print(str[i], end="")

for i in range(0, 4, 2):  # 2번째 파라미터는 n-1이다.
    print("hello")
