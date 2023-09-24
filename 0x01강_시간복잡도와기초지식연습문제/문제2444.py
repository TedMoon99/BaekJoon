# 별 찍기 - 7
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어보거라

N = int(input())
for i in range(N):
  star = ' ' * (N - i - 1) + '*' * (2 * (i+1) - 1)
  print(star)
for j in range(N-1):
  star = ' ' * (j + 1) + '*' * (2 * (N-j-1) - 1)
  print(star)
  