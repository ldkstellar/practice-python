while True:
    try:
        a, b = map(int, input("숫자를 입력하세요.\n").split(","))
        print(a, b)

    except:
        print("숫자만 입력하세요\n")
