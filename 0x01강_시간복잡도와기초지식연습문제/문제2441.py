# 별 찍기 - 4
# 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ... , N번째 줄에는 별 1개를 찍는 문제
# 하지만, 오른쪽을 기준으로 정렬한 별을 출력하기
N = int(input())

for i in range(N):
  star = ' ' * i +'*' * (N - i)
  print(star)