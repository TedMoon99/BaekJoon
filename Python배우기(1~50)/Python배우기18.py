# 소인수 분해
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

n = int(input())
i = 2
while i <= n:
    while n % i == 0:
        print(i)
        n = n // i 
    i += 1
