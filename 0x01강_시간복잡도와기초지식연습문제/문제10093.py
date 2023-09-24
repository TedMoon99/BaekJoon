# 숫자
# 두 양의 정수가 주어질 경우 두 수 사이에 있는 정수를 모두 출력
a, b = map(int, input().split())

print(b-a-1)
list = []
for i in range(a, b + 1):
  list.append(str(i))

result = ' '.join(list)
print(result)
  