# 윤년
year = int(input())

# 윤년 : 연도가 4의 배수 and 100의 배수가 아닌경우 or 400의 배수

if not (year % 400) or (not year % 4 and year % 100 != 0):
  print(1)
else:
  print(0)