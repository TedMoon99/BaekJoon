# 주사위 세개
a, b, c = map(int, input().split())
if a ==b and b == c:
    price = 10000 + a * 1000
    print(price)
elif (a == b and a != c) or (a ==c and a != b) or (b == c and b != a):
    if a == b:
        price = 1000 + a * 100
    elif a == c:
        price = 1000 + a * 100
    else:
        price = 1000 + b * 100
    print(price)
else:
    maxPrice = max(a, b, c)
    price = 100 * maxPrice
    print(price)
