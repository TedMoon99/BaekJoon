# 숫자
# 두 양의 정수가 주어질 경우 두 수 사이에 있는 정수를 모두 출력
def fun(num1, num2):
  # 두 수 사이에 있는 수의 개수를 출력
  print(abs(num2-num1) - 1)
  # 두 수 사이에 있는 수를 오름차순으로 출력
  if num1 < num2:
    for i in range(num1+1, num2):
      print(i, end=' ')
  else:
    for i in range (num2+1, num1):
      print(i, end=' ')

a, b = map(int, input().split())
fun(a, b)


