# 알파벳 개수
S = input()
# 아스키코드 소문자 a = 97 ~ z = 122
result = [0] * 26
for s in S:
  for j in range(97, 123):
    if s == chr(j):
      result[j-97] += 1

for i in range(len(result)):
  print(result[i], end= ' ')