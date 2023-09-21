# 주사위 세개
x, y, z = map(int, input().split())
# 가격결정 함수
def makePrice(signal, number = 0):
  if signal == 0:
    return 10000 + 1000 * number
  elif signal == 1:
    return 1000 + number * 100    
  elif signal == 2:
    return number * 100
  else:
    print("잘못된 signal입니다. signal을 확인해주세요.")

# 1 ~ 6
price = 0
if x == y and y == z: # signal = 0
  price = makePrice(0, x)
elif x == y and x != z: # signal = 1
  price = makePrice(1, y)
elif x == z and z != y: # signal = 1
  price = makePrice(1, x)
elif z == y and x != y: # signal = 1
  price = makePrice(1, z)
else: # signal = 2
  price = makePrice(2, max(x, y, z))

print(price)