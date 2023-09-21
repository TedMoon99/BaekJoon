# 최댓값
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
numbers = []
for i in range(9):
  numbers.append(int(input()))

# 최댓값을 찾기
maxValue = max(numbers)
maxIndex = numbers.index(maxValue) + 1

# 최댓값과 몇 번째 수인지 출력
print(maxValue)
print(maxIndex)
