# 세 수
# 입력 받아오기
array = input().split()
# 문자열 리스트 -> 정수 리스트
for i in range(len(array)):
    array[i] = int(array[i])
# 최댓값을 찾기
currentMax = max(array)
# 리스트에서 최대값 제거
array.remove(currentMax)
print(max(array))