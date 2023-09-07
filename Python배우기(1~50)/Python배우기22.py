# 최소공배수
import math
def glc(a, b):
    gcd = math.gcd(a, b)
    if a == 1 or b == 1: # 둘 중 하나가 1인 경우
        return a * b
    elif a == b: # 둘이 같은 숫자인 경우
        return a
    elif gcd == 1:# a와 b가 서로소인 경우
        return a * b
    else: # 이 부분을 좀 더 효율적으로 처리해야함....
        a = a // gcd
        b = b // gcd
        return a * b * gcd
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    result = glc(a,b)
    print(result)

