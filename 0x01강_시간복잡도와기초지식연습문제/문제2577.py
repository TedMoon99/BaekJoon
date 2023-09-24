# 숫자의 개수
# A x B x C 를 계산한 결과에 0부터 9까지 각각읭 숫자가 몇 번씩 쓰였는지를 구하는 프로그램
# 첫째 줄에는 A x B x C의 결과에 0이 몇 번 쓰였는지 출력
# 둘째 줄 ~ 열 번째 줄까지 1~9까지의 숫자가 각각 몇 번 쓰였는지를 한 줄에 하나씩 출력
def checkFun(number):
  number = str(number)
  numlist = [0] * 10
  for i in range(10):
    numlist[i] = number.count(str(i))
  return numlist


result = 1
for _ in range(3):
  result *= int(input())

resultList = checkFun(result)
for j in range(10):
  print(resultList[j])
