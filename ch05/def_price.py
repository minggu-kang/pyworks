# 전역변수의 범위  예제


def price():
    price = 250 * quantity
    print("{}원 입니다.".format(price))


quantity = 2
print("{}개에".format(quantity))
price()

