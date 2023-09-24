# 별 찍기 - 8
# 예제를 보고 규칙을 유추한 뒤에 별을 찍기
N = int(input())

for i in range(N):
  star = '*' * (i+1) + ' ' * (2 * (N - i - 1)) + '*' * (i+1)
  print(star)
for j in range(N-1):
  star = '*' * (N - j - 1) + ' ' * (2*(j+1)) + '*' * (N - j - 1)
  print(star)