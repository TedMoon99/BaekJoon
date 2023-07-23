# 과자
k, n, m = map(int, input().split())
# 부모님께 받아야 하는 모자란 돈을 계산
needMoney = k * n - m
if needMoney <= 0:
    print(0)
else:
    print(needMoney)