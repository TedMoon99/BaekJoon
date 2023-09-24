# 별 찍기 - 9
N = int(input())
for i in range(N):
  star = ' ' * i + '*' * (2 * (N - i)-1)
  print(star)
for j in range(N-1):
  star = ' ' * (N-j-2) + '*' * (2 * (j+1) + 1)
  print(star)
  