# 숫자
# 두 양의 정수가 주어질 경우 두 수 사이에 있는 정수를 모두 출력
a, b = map(int, input().split())
def fun(a, b): # a가 b보다 작다고 가정
  temp = []
  print(b-a-1)
  for i in range(a+1, b):
    print(i, end=' ')

if a >=b :
  fun(b, a)
else:
  fun(a, b)