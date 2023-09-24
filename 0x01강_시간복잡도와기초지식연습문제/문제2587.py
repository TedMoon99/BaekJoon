# 대표값2
# 입력 받아오기
numbers = []
for _ in range(5):
  numbers.append(int(input()))
# 평균 계산하기
avg = sum(numbers)// 5
# 중앙값 계산하기
numbers.sort()
mid = numbers[2]
# 출력하기
print("------구분선------")
print(avg)
print(mid)