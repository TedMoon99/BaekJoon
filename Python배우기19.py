# 수들의 합
# 서로다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

n = int(input())
i = 1
while n >=0:
    n -= i
    i += 1
print(i-2)
