# 별 찍기 - 6
# 첫째 줄에는 별 2N-1개, 둘째 줄에는 별 2N-3개, ..., N번째 줄에는 별 1개를 찍는 문제

N = int(input())
for i in range(N):
  star = ' ' * i + '*' * (2 * (N - i) - 1)
  print(star)