class Star:
    type = "star"
    x = 100

    def change():
        x = 200
        print('x is', x)

print('x is', Star.x)
Star.change()
print('x is', Star.x)

star = Star()  # 굳이 객체를 생성하는 것도 가능?
print('x is', star.x)  # 객체 변수로 액세스 하지만, 뭘로 귀착? 클래스 변수 x를 가리킨다.
star.change()

# self가 없는 클래스는 객체 생성용이 아니라 그루핑용이다