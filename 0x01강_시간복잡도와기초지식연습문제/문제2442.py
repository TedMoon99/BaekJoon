# 별 찍기 - 5
# 첫째 줄에는 별 1개, 둘째 줄에는 별 3개, ... , N번째 줄에는 별 2xN-1개를 찍는 문제
# 별은 가운데를 기준으로 대칭이어야 한다.
N = int(input())
for i in range(N):
  star = ' ' * (N - (i+1)) + '*' * (2*(i+1)-1)
  print(star)