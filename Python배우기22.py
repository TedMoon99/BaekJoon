# 최소공배수
import math
def glc(a, b):
    if a == 1 or b == 1: # 둘 중 하나가 1인 경우
        return a * b
    elif a == b: # 둘이 같은 숫자인 경우
        return a
    elif math.gcd(a,b) == 1:# a와 b가 서로소인 경우
        return a * b
    else: 
        for i in range(1, a+1):
            for j in range(1, b+1):
                if a * j == b * i:
                    return a * j
        return "Wrong Code"
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    result = glc(a,b)
    print(result)

