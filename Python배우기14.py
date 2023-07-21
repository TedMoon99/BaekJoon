# 문자열 반복
t = int(input())
for i in range(t):
    r, s = input().split()
    r = int(r)
    result = ''
    for j in range(len(s)):
        result += s[j] * r
    print(result)

