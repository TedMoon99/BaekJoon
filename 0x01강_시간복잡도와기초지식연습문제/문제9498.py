# 시험 성적
# 문제 : 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 시험 점수가 주어진다. 0 ≤ 시험점수 ≤ 100
# 출력 : 시험 성적을 출력한다.
score = int(input())
if score >= 90 and score <= 100:
  print('A')
elif score >= 80 and score < 90:
  print('B')
elif score >= 70 and score < 80:
  print('C')
elif score >= 60 and score < 70:
  print('D')
else:
  print('F')
