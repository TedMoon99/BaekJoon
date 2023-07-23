# 주사위 게임
t = int(input())
temp = []
for i in range(t):
    a, b, c = map(int, input().split())
    if a ==b and b == c:
        price = 10000 + a * 1000
        temp.append(price)
    elif (a == b and a != c) or (a ==c and a != b) or (b == c and b != a):
        if a == b:
            price = 1000 + a * 100
        elif a == c:
            price = 1000 + a * 100
        else:
            price = 1000 + b * 100
        temp.append(price)
    else:
        maxPrice = max(a, b, c)
        price = 100 * maxPrice
        temp.append(price)
print(max(temp))