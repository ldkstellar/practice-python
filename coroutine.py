def number_coroutine():
    while True: #코루틴을 유지하기 위해 무한 루프 사용
        x = (yield) #코루틴 바깥에서 값을 받아온다.
        print(x)

co = number_coroutine()
next(co)# 코투린함수가 yield까지 실행되고 멈춤
co.send(1)
print("hello1")
co.send(2)
print("hello2")
co.send(3)
print("hello3")