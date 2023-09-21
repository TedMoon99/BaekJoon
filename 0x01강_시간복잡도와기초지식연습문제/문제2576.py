# 홀수
# 7개의 자연수가 주어질 때
# 홀수를 찾아 합을 구하고 / 홀수들 중에서 최솟값을 찾아라
oddList = []
for _ in range(7):
  temp = int(input())
  if temp % 2:
    oddList.append(temp)
    continue
if not len(oddList):
  print(-1)
else:
  print(sum(oddList))
  print(min(oddList))
