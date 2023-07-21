# 소음
# only + and *
# 숫자는 모두 10의 제곱형태 | 최대 100자리수

a = int(input())
op = input()
b = int(input())
if op == '+':
    print(a+b)
elif op == '*':
    print(a*b)
else:
    print("Wrong input")