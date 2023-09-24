# 핸드폰 요금
# 영식 요금제 30초마다 10원
# 민식 요금제 60초마다 15원
# 통화 시간 목록이 주어질 경우 어느 요금제를 사용하는 것이 저렴한지 출력

def costA(time): # 영식 요금제
  if time < 30:
    return 10
  else:
    return costA(time - 30) + 10

def costB(time): # 민식 요금제
  if time < 60:
    return 15
  else:
    return costB(time- 60) + 15

N = int(input())
timeList = input().split()
for i in range(N):
  timeList[i] = int(timeList[i])

payA, payB = 0, 0

for j in range(N):
  payA += costA(timeList[j])
  payB += costB(timeList[j])

if payA > payB:
  print('M', payB)
elif payA < payB:
  print('Y', payA)
else:
  print('Y', 'M', payA)